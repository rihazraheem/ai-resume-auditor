from config import Config
from security import ContentSecurity
from llama_index.llms.groq import Groq
import logging

logger = logging.getLogger("ResumeAuditor")

class LLMFeedback:
    _llm = Groq(model=Config.LLM_MODEL_NAME, api_key=Config.GROQ_API_KEY)

    @staticmethod
    def get_llm_keyword_analysis(resume_text, jd_text):
        safe_resume = ContentSecurity.sanitize_resume(resume_text)
      
        prompt = f"""
        You are a Senior Technical Recruiter. Analyze this Resume against the Job Description (JD).

        1. Found: List key technical skills from the JD present in the resume.
        2. Missing: List critical skills/tools from the JD not found in the resume.
        3. Recommendations: Provide 3 specific, actionable bullet points to improve the match.
        4. Reasoning: A 1-sentence summary of the overall fit.

        Format the output strictly as:
        Found: [list]
        Missing: [list]
        Recommendations: [bullet points]
        Reasoning: [1 sentence]

        JD: {jd_text}
        Resume Snippet: {safe_resume[:4000]}
        """

        try:
            response = LLMFeedback._llm.complete(prompt)
            return response.text
        except Exception as e:
            logger.error(f"LLM Feedback Error: {e}")
            return "Feedback is currently unavailable. Please try again later."
