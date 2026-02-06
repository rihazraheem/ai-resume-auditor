import re
from config import Config
from resources import get_nlp

class InfoExtractor:
    @staticmethod
    def get_details(text):
        email=next(iter(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)), "Unknown")
        phone_pattern=r'(?:\+91[\-\s]?)?[6-9]\d{4}[\-\s]?\d{5}|\d{10}'
        phones=re.findall(phone_pattern, text)
        phone=phones[0] if phones else "Unknown"
        nlp=get_nlp()
        doc=nlp(text[:500])
        name="Unknown"
        for ent in doc.ents:
            if ent.label_=="PERSON":
                name=ent.text
                break
        if name=="Unknown":
            lines=[line.strip() for line in text.split('\n') if line.strip()]
            if lines:
              name=lines[0][:50]

        return name, email, phone
