import streamlit as st
from resume_parser import ResumeParser
from extractor import InfoExtractor
from similarity import HybridSimilarity
from llm_feedback import LLMFeedback
from database import save_entry
from config import Config

st.set_page_config(page_title="AI Resume Auditor", layout="wide")
st.title("🚀 AI Resume Auditor & Matcher")
st.markdown("Upload your resume to see how well it matches the Job Description and get AI-powered improvement tips.")
st.sidebar.info("Recruiters: Go to the 'HR Portal' in the sidebar to view candidates.")

col1, col2=st.columns(2)

with col1:
    st.subheader("1. Job Description")
    jd_input=st.text_area("Paste the Job Description here:", height=300, placeholder="Looking for a Python Developer with experience in...")

with col2:
    st.subheader("2. Upload Resume")
    uploaded_file=st.file_uploader("Upload PDF or DOCX", type=list(Config.ALLOWED_EXTENSIONS))

if st.button("Analyze Resume"):
    if not jd_input or not uploaded_file:
        st.error("Please provide both a Job Description and a Resume.")
    else:
        with st.status("Analyzing...", expanded=True) as status:
            st.write("Extracting text...")
            resume_text=ResumeParser.extract_text(uploaded_file.read(), uploaded_file.name)
            name, email, phone=InfoExtractor.get_details(resume_text)
            
            st.write("Cleaning Job Description...")
            clean_jd=ResumeParser.clean_job_description(jd_input)
            
            st.write("Calculating Match Score...")
            score, sbert, tfidf = HybridSimilarity.calculate_hybrid_score(resume_text, clean_jd)
            
            status.update(label="Analysis Complete!", state="complete", expanded=False)

        st.divider()
        col_metric,=st.columns(1)
        col_metric.metric("Overall Match Score", f"{score}%")

        if score >= Config.MATCH_THRESHOLD:
            st.success(f"Great match, {name}! Your resume is highly compatible with this role.")
        else:
            st.warning(f"Hello {name}, your match score is a bit low. Check the recommendations below.")

        st.subheader("💡 AI Recruiter Feedback")
        with st.spinner("Generating detailed suggestions..."):
            feedback=LLMFeedback.get_llm_keyword_analysis(resume_text, jd_input)
            st.markdown(feedback)
