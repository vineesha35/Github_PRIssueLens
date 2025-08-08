# 🔍 GitHub PR/Issue Summarizer

This application summarizes GitHub pull requests (PRs) and issues — including their comments — to provide **key insights** and **actionable next steps**.  
It uses the **GROQ API** for summarization and the **GitHub API** for data retrieval.





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

- 1️⃣ **Enter API Tokens**
GROQ API Key → Enter in the "Settings" section of the sidebar.

GitHub Token (optional) → Generate from GitHub with repo scope and paste it in the "GitHub Token" field in the sidebar.

2️⃣ **Input GitHub URL**
Paste the GitHub pull request or issue URL:

arduino
Copy
Edit
https://github.com/owner/repo/pull/123



