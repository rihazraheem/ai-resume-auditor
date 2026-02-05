import re
class ContentSecurity:
    @staticmethod
    def sanitize_resume(text):
        """Removes PII before LLM processing."""
        text=re.sub(r'\S+@\S+', '[EMAIL_REDACTED]', text)
        phone_pattern=r'(\+91[\-\s]?)?[6-9]\d{4}[\-\s]?\d{5}|\b\d{10}\b'
        text=re.sub(phone_pattern, '[PHONE_REDACTED]', text)
        return text
