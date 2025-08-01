
# 🧠 AI Resume Optimizer

This project is an **AI-powered resume optimizer** that:
- Accepts your resume and job description
- Uses a Hugging Face model (e.g., LLaMA3/Gemma via Transformers) to rewrite the resume
- Generates suggestions and a downloadable `.docx` resume
- Supports frontend via Streamlit and backend via FastAPI

## 🚀 Features

✅ Upload resume in `.docx` or `.pdf`  
✅ Paste or type job description  
✅ Optimized resume using open-source LLM  
✅ Download structured `.docx` output  
✅ Supports profile photo, GitHub, LinkedIn links  
✅ ATS-friendly format with sections: Summary, Education, Experience, Projects, Skills

## 🖥️ Tech Stack

| Layer     | Technology Used         |
|-----------|--------------------------|
| Frontend  | Streamlit                |
| Backend   | FastAPI + Hugging Face Transformers |
| LLM       | Local Hugging Face models (LLaMA, Gemma, etc.) |
| Resume    | `python-docx`, `PyMuPDF` |
| Packaging | `requests`, `base64`, `pydantic` |

## 📦 Project Structure

```
resume_optimizer/
├── app/
│   ├── main.py                # FastAPI backend
│   ├── models.py              # Pydantic schemas
│   ├── llm_handler.py         # HuggingFace model interface
│   ├── utils.py               # .docx generation utilities
│   ├── extractor.py           # (optional) .pdf/.docx text extractor
├── frontend/
│   └── app.py                 # Streamlit UI
├── requirements.txt
├── README.md
```

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/resume-optimizer
cd resume-optimizer
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

It will start at: http://127.0.0.1:8000

### 5. Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

## 📥 Sample API Call

```http
POST /optimize_resume/
Content-Type: application/json

{
  "resume_text": "John Doe, Python Developer...",
  "job_description": "We are hiring a FastAPI backend engineer..."
}
```

Response:
```json
{
  "suggestions": "• Tailor experience to highlight FastAPI usage...",
  "docx_base64": "<base64-encoded-doc>"
}
```

## ✨ Example Output

- Clean `.docx` resume with:
  - Bold + underlined section headers
  - Bullet point content
  - Optional profile photo
  - Clickable LinkedIn/GitHub links

## 🔗 Links

- GitHub: [Ashiyarana12](https://github.com/Ashiyarana12)
- (Add LinkedIn & Portfolio here once ready)

## 📃 License

MIT License. Free to use, modify, and extend.
