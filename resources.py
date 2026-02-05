import spacy
from config import Config
import logging

logger=logging.getLogger("ResumeAuditor")
_nlp=None

def get_nlp():
    global _nlp
    if _nlp is None:
        try:
            _nlp=spacy.load(Config.SPACY_MODEL_NAME)
        except OSError:
            logger.info("Downloading spaCy model...")
            spacy.cli.download(Config.SPACY_MODEL_NAME)
            _nlp=spacy.load(Config.SPACY_MODEL_NAME)
    return _nlp
