import streamlit as st
import requests
import re

st.set_page_config(page_title="GitHub PR/Issue Summarizer", layout="wide")
st.title("🔍 GitHub PRIssueLens")

# --- Sidebar Settings ---
st.sidebar.header("🔐 API Settings")
groq_api_key = st.sidebar.text_input("GROQ API Key", type="password")
github_token = st.sidebar.text_input("GitHub Token (optional)", type="password")

# --- Checkbox Options ---
st.sidebar.header("⚙️ Options")
include_comments = st.sidebar.checkbox("Include Comments", value=True)
include_metadata = st.sidebar.checkbox("Include Metadata", value=True)
use_custom_prompt = st.sidebar.checkbox("Use Custom Prompt")
custom_prompt = ""
if use_custom_prompt:
    custom_prompt = st.sidebar.text_area("Enter your custom prompt")

# --- URL Input ---
st.subheader("Paste GitHub PR/Issue URL")
github_url = st.text_input("Example: https://github.com/owner/repo/pull/123")

# --- Trigger Button ---
if st.button("Summarize"):

    if not github_url or not groq_api_key:
        st.warning("Please enter a GitHub URL and your GROQ API Key.")
        st.stop()

    # Extract details from URL
    match = re.match(r"https://github\.com/(.*?)/(.*?)/(pull|issues)/(\d+)", github_url)
    if not match:
        st.error("Invalid GitHub URL format.")
        st.stop()

    owner, repo, item_type, number = match.groups()
    headers = {"Accept": "application/vnd.github+json"}
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"

    # Fetch issue or PR details
    url_type = "issues" if item_type == "issues" else "pulls"
    base_url = f"https://api.github.com/repos/{owner}/{repo}/{url_type}/{number}"
    response = requests.get(base_url, headers=headers)

    if response.status_code != 200:
        st.error("Failed to fetch GitHub data.")
        st.stop()

    data = response.json()
    summary_input = []

    if include_metadata:
        st.markdown("### 📝 Metadata")
        st.write({
            "title": data.get("title"),
            "author": data.get("user", {}).get("login"),
            "state": data.get("state"),
            "created_at": data.get("created_at"),
            "labels": [label["name"] for label in data.get("labels", [])]
        })

        summary_input.append(f"Title: {data.get('title')}")
        summary_input.append(f"Author: {data.get('user', {}).get('login')}")
        summary_input.append(f"State: {data.get('state')}")
        summary_input.append(f"Created At: {data.get('created_at')}")
        summary_input.append(f"Labels: {', '.join([label['name'] for label in data.get('labels', [])])}")

    summary_input.append(f"\n---\n{data.get('body') or 'No description'}")

    # Fetch comments if selected
    if include_comments:
        comments_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{number}/comments"
        comments_res = requests.get(comments_url, headers=headers)

        if comments_res.status_code == 200:
            comments = comments_res.json()
            st.markdown("### 💬 Comments")
            for c in comments:
                st.write(f"{c['user']['login']}: {c['body']}")
                summary_input.append(f"{c['user']['login']}: {c['body']}")

    # Prompt for GROQ
    prompt = custom_prompt or (
        "Summarize the following GitHub issue or PR in a concise way. "
        "Include key points, important comments, and next actionable steps.\n\n"
        + "\n\n".join(summary_input)
    )

    st.markdown("### 🧠 Summary")
    # GROQ API call
    groq_headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    groq_payload = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "model": "llama3-70b-8192"
    }

    groq_res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=groq_headers, json=groq_payload)
    if groq_res.status_code == 200:
        result = groq_res.json()
        st.success("Summary generated successfully!")
        st.markdown(result["choices"][0]["message"]["content"])
    else:
        st.error(f"Failed to generate summary from GROQ API.\nStatus Code: {groq_res.status_code}")
        st.code(groq_res.text, language='json')

