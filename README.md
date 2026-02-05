# 🚀 AI Resume Auditor & Matcher

A production-ready, modular AI application that analyzes resumes against Job Descriptions using **SBERT Semantic Search**, **TF-IDF Keyword Matching**, and **LLM-powered feedback** via Groq.

## ✨ Features
* **Dual-Portal System**: Private sandbox for candidates and a protected dashboard for HR.
* **Hybrid Scoring**: Combines contextual meaning (SBERT) with exact skill matching (TF-IDF).
* **PII Security**: Automatically redacts emails and phone numbers before sending data to cloud LLMs.
* **Bulk Processing**: HR can upload and score multiple resumes simultaneously.
* **AI Feedback**: Provides actionable bullet points and reasoning using Llama-3.

## 🏗️ Architecture
The project follows a **Service-Oriented Architecture (SOA)** for scalability and maintenance:
* `Candidate_portal.py`: Public entry point.
* `pages/HR_Portal.py`: Protected recruitment dashboard.
* `services/`: Modular logic for parsing, scoring, and security.
* `resources.py`: Singleton manager for heavy AI models.

## 🛠️ Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/rihasraheem/ai-resume-auditor.git](https://github.com/rihasraheem/ai-resume-auditor.git)
cd ai-resume-auditor

### 2. Install Dependencies

* pip install -r requirements.txt

* python -m spacy download en_core_web_sm

### 3. Environment Variables
* Create a secrets manager or set the following environment variables:

* GROQ_API_KEY: Your Groq API Key.

* HR_USERNAME: Admin username for the portal.

* HR_PASSWORD: Admin password for the portal.

## 🚀 Deployment

* This app is optimized for Streamlit Community Cloud.

* Connect your GitHub repo to Streamlit Cloud.

* Add your environment variables to the Secrets tab in the dashboard.

* Ensure requirements.txt and packages.txt are in the root directory.

