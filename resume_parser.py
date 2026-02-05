import fitz
import docx
import io
import re
import logging
from config import Config
from resources import get_nlp

logger=logging.getLogger("ResumeAuditor")

class ResumeParser:
    @staticmethod
    def extract_text(file_bytes, filename):
        ext=filename.split('.')[-1].lower()
        try:
            if ext=='pdf':
                return ResumeParser._from_pdf(file_bytes)
            elif ext=='docx':
                return ResumeParser._from_docx(file_bytes)
            else:
                return ""
        except Exception as e:
            logger.error(f"Failed to parse {filename}: {e}")
            return ""

    @staticmethod
    def _from_pdf(file_bytes):
        text=""
        with fitz.open(stream=file_bytes, filetype="pdf") as doc:
            for page in doc:
                text+=page.get_text()
        return ResumeParser.basic_clean(text)

    @staticmethod
    def _from_docx(file_bytes):
        doc=docx.Document(io.BytesIO(file_bytes))
        text="\n".join([para.text for para in doc.paragraphs])
        return ResumeParser.basic_clean(text)

    @staticmethod
    def basic_clean(text):
        text=re.sub(r'\s+', ' ', text)
        return text.strip()

    @staticmethod
    def clean_job_description(jd_text):
        nlp=get_nlp()
        doc=nlp(jd_text.lower())
        clean_terms=[
            token.text for token in doc 
            if token.pos_ in ['NOUN', 'PROPN', 'ADJ'] and not token.is_stop
        ]
        return " ".join(clean_terms)
