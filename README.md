# 🔍 GitHub PR/Issue Summarizer

Ever opened a GitHub pull request… only to find a scroll-fest of comments, debates, and code suggestions?
This app is your developer sidekick — it dives into the chaos, reads everything (PRs, issues, and comments), and comes back with a crisp, human-friendly summary plus actionable next steps.

Powered by the GROQ LLM API for lightning-fast AI summaries and the GitHub API for precise data fetching, it’s built for:

🏃‍♂️ Busy maintainers who want to skip the fluff

🛠️ Teams tired of “I’ll read it later” PRs

📌 Anyone who wants decisions and context in seconds

Just paste a PR or issue link, and the app handles the rest — from fetching metadata to condensing endless discussions into something you can actually read during a coffee break. ☕





https://github.com/user-attachments/assets/1137e8c9-3cab-4186-828f-472d162e68f2


---

## ✨ Features
- 📄 **Summarizes** GitHub pull requests and issues, including all comments.
- 📝 **Provides concise summaries** and actionable next steps for better understanding.
- 🔒 **Handles private repositories** with authentication using a GitHub Personal Access Token.
- 🚀 **Avoids rate limits** by authenticating with a GitHub token.

---

## 📋 Prerequisites
- **Python 3.8** or higher
- A valid **GROQ API Key** for summarization
- *(Optional)* A **GitHub Personal Access Token** — recommended for increased API rate limits or private repositories.

---

## 🚀 Usage

*Enter API Tokens*
 - GROQ API Key → Enter in the "Settings" section of the sidebar.

 - GitHub Token (optional) → Generate from GitHub with repo scope and paste it in the "GitHub Token" field in the sidebar.

## Input GitHub URL

- Paste the GitHub pull request or issue URL (e.g., `https://github.com/owner/repo/pull/123`) into the input box and press Enter.

---

## View Results

- **Details:**
  - Displays metadata about the PR/issue, including state, author, creation date, and labels.

- **Summary:**
  - A concise overview and actionable next steps generated using the GROQ API.

---

## Dependencies

Run the following command in your terminal to install the required dependencies:

```bash
pip install streamlit requests groq python-dotenv
```
## Run the application
Run the following command in your terminal to start the Streamlit application:
```bash
streamlit run app.py
```
## Author
 Made by Vineesha Avasarala 2025






