# Digital Identity - LinkedIn & GitHub Integration

A FastAPI and Streamlit-based application designed to showcase a professional portfolio by integrating real-time data from LinkedIn (via OAuth 2.0) and GitHub.

## 🚀 Features
- **LinkedIn OAuth 2.0 Integration**: Securely authenticates users and fetches professional profile data (OpenID Connect).
- **GitHub API Integration**: Retrieves repository and project data to showcase technical work.
- **FastAPI Backend**: A modular backend service following clean architectural patterns.
- **Streamlit Frontend**: A lightweight, interactive dashboard to display professional identity.

## 🛠️ Tech Stack
- **Backend**: Python 3.12, FastAPI, Uvicorn
- **Frontend**: Streamlit
- **APIs**: LinkedIn REST API, GitHub API
- **Utilities**: Requests, Dotenv, Python-Multipart

## 📁 Project Structure
```text
Digital_Identity/
├── backend/
│   ├── main.py              # FastAPI entry point & routes
│   └── service/
│       ├── linkedin.py      # LinkedIn OAuth logic & API calls
│       └── github.py        # GitHub API integration logic
├── frontend/
│   └── home.py              # Streamlit dashboard
├── .env                     # Environment variables (Secrets)
├── .gitignore               # Files excluded from Git
└── requirements.txt         # Project dependencies