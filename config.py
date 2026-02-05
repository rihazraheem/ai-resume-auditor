import os

class Config:
    HR_USERNAME=os.environ.get('HR_USERNAME', 'admin')
    HR_PASSWORD=os.environ.get('HR_PASSWORD')
    GROQ_API_KEY=os.environ.get('GROQ_API_KEY')

    SBERT_MODEL_NAME='all-MiniLM-L6-v2'
    LLM_MODEL_NAME="llama-3.3-70b-versatile"
    SPACY_MODEL_NAME="en_core_web_sm"

    MATCH_THRESHOLD=45.0
    ALLOWED_EXTENSIONS={'pdf', 'docx'}
    DB_URL="sqlite:///hr_database.db"
