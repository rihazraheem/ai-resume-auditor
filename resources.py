import spacy
from config import Config
import logging

logger=logging.getLogger("ResumeAuditor")
_nlp=None

def get_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("en_core_web_sm")
    return _nlp
