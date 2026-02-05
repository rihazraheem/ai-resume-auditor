import streamlit as st
from auth import AuthManager
from resume_parser import ResumeParser
from extractor import InfoExtractor
from similarity import HybridSimilarity
from database import save_entry, get_df
from config import Config

if not AuthManager.login():
    st.stop()

st.title("💼 Recruiter Dashboard")
st.markdown("Process candidates and manage the applicant database.")

with st.expander("📝 Set Active Job Description", expanded=True):
    hr_jd = st.text_area("Paste the JD here to score candidates against it:", height=200)

st.subheader("📤 Bulk Candidate Upload")
uploaded_files = st.file_uploader(
    "Select multiple resumes (PDF/DOCX)", 
    type=list(Config.ALLOWED_EXTENSIONS), 
    accept_multiple_files=True
)

if st.button("Start Batch Processing") and hr_jd:
    if not uploaded_files:
        st.warning("Please upload files first.")
    else:
        clean_jd=ResumeParser.clean_job_description(hr_jd)
        progress_bar=st.progress(0)
        
        for idx, file in enumerate(uploaded_files):
            raw_text=ResumeParser.extract_text(file.read(), file.name)
            name, email, phone=InfoExtractor.get_details(raw_text)
            score, _, _ = HybridSimilarity.calculate_hybrid_score(raw_text, clean_jd)
            
            save_entry(name, email, phone, file.name, score)
            
            progress_bar.progress((idx + 1) / len(uploaded_files))
        
        st.success(f"Processed {len(uploaded_files)} resumes successfully!")
        st.rerun()

st.divider()
st.subheader("🏆 Candidate Leaderboard")
df = get_df()

if not df.empty:
    df=df.sort_values(by="score", ascending=False)
  
    status_filter=st.multiselect("Filter by Status:", ["Pass", "Fail"], default=["Pass", "Fail"])
    st.dataframe(df[df['status'].isin(status_filter)], use_container_width=True)

    csv=df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Excel/CSV Report", data=csv, file_name="candidate_report.csv")
else:
    st.info("Database is empty. Upload resumes above to see results.")
