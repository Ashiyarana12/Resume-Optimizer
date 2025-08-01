import streamlit as st
import requests
import base64
import docx
import fitz  # PyMuPDF

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file):
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in pdf:
        text += page.get_text()
    return text

st.set_page_config(page_title="AI Resume Optimizer", layout="wide")

st.title("🧠 Smart Resume Optimizer using Open-Source LLM")

st.sidebar.header("Upload Resume")
uploaded_file = st.sidebar.file_uploader("Upload your resume (.docx or .pdf)", type=["docx", "pdf"])

st.sidebar.header("Job Description")
job_description = st.sidebar.text_area("Paste Job Description here", height=200)

st.sidebar.header("Track Applications")
if st.sidebar.button("Show Application Status"):
    st.sidebar.success("You’ve applied to 3 jobs. Last: Software Engineer @ OpenAI - Status: Pending")

st.markdown("---")

if uploaded_file and job_description:
    st.success("Resume and Job Description received ✅")

    if st.button("✨ Optimize Resume Using HuggingFace Model"):
        with st.spinner("Extracting and sending data to LLM..."):
            try:
                if uploaded_file.name.endswith(".docx"):
                    resume_text = extract_text_from_docx(uploaded_file)
                elif uploaded_file.name.endswith(".pdf"):
                    resume_text = extract_text_from_pdf(uploaded_file)
                else:
                    st.error("Unsupported file format.")
                    resume_text = ""

                payload = {
                    "resume_text": resume_text,
                    "job_description": job_description
                }

                response = requests.post("http://localhost:8000/optimize_resume/", json=payload)

                if response.status_code == 200:
                    result = response.json()
                    st.subheader("🔍 LLM Suggestions:")
                    st.markdown(result["suggestions"])
                    
                    st.download_button("📥 Download Updated Resume (DOCX)",
                                       data=base64.b64decode(result["docx_base64"]),
                                       file_name="Optimized_Resume.docx")
                else:
                    st.error("❌ LLM backend error. Please check FastAPI logs.")
            except Exception as e:
                st.exception(f"❌ Something went wrong: {e}")
else:
    st.info("👈 Upload your resume and paste a job description to get started.")

st.markdown("---")
st.caption("Built with ❤️ using HuggingFace, Streamlit & FastAPI")
