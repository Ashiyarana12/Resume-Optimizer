from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import ResumeRequest
from app.llm_handler import query_llm
from app.utils import create_template_resume_docx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/optimize_resume/")
async def optimize_resume(data: ResumeRequest):
    try:
        # Enhanced prompt for better structured output from the LLM
        prompt = f"""
You are an expert AI resume writer. Your task is to rewrite a given resume to perfectly match a job description,
ensuring it is highly ATS-friendly and follows a strict, well-defined structure.

**Instructions for Output:**
1.  **Format:** Return the result in plain text.
2.  **Structure:** Adhere strictly to the following six numbered sections. Each section MUST start with its exact title, followed by its content.
    * 1. Name + Contact Info
    * 2. Summary
    * 3. Education
    * 4. Experience
    * 5. Projects
    * 6. Skills
3.  **Content:**
    * Tailor all content (Summary, Experience, Projects, Skills) to align with the keywords and requirements of the JOB DESCRIPTION.
    * Use strong action verbs in Experience and Project descriptions.
    * Quantify achievements wherever possible.
    * Ensure contact information is clear.
    * For Skills, categorize them if appropriate (e.g., Programming Languages, Frameworks, Tools).
4.  **Exclusions:**
    * Do NOT include any introductory or concluding remarks outside of the structured resume content.
    * Do NOT include the job description again in the response.
    * Do NOT include any conversational text, explanations, or markdown formatting (like ```text).
    * Do NOT include any content that is not part of the resume sections.

**RESUME TO OPTIMIZE:**
{data.resume_text}

**JOB DESCRIPTION:**
{data.job_description}

**BEGIN REWRITTEN RESUME:**
"""
        rewritten_resume = query_llm(prompt)
        # --- DEBUGGING OUTPUT ---
        print("--- LLM Raw Output Start ---")
        print(rewritten_resume)
        print("--- LLM Raw Output End ---")
        # ------------------------
        docx_base64 = create_template_resume_docx(rewritten_resume)

        return {
            "suggestions": rewritten_resume,
            "docx_base64": docx_base64
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
