# **AI Summarizer (Text, PDF, YouTube)**

A full-stack AI summarization tool that supports summarizing plain text, PDF documents, and YouTube video transcripts using the Groq Llama 3 model.
The project includes a React frontend and a Flask backend.

Features

- Summarize plain text
- Upload and summarize PDF documents 
- Summarize YouTube video transcripts
- Fast responses using OpenAI GPT-3.5-Turbo
- Backend built with Flask
- Frontend built with React
- Secure environment variable handling

**Tech Stack**
Frontend
- React
- Axios
Backend
- Python
- Flask
- OpenAI Python SDK
- PyMuPDF (fitz) for PDF text extraction
- YouTube Transcript API
- Flask-CORS

**Installation and Setup**
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd AISUMMARIZER

**Backend Setup (Flask + OpenAI)**
Navigate to the backend folder:
cd backend

Create a virtual environment:
python -m venv env

Activate the environment:
.\env\Scripts\Activate.ps1     (PowerShell)

Install backend dependencies:
pip install -r requirements.txt
Create a .env file in the backend directory:
OPENAI_API_KEY=your_actual_api_key_here

Run the backend:
python app.py
Backend runs at:
http://127.0.0.1:5000

**Frontend Setup (React)**
Open a new terminal window and navigate to the frontend directory:
cd frontend
npm install
npm start

Frontend runs at:
http://localhost:3000

**Notes**
- Requires an active OpenAI API key from https://platform.openai.com
- GPT-3.5-Turbo usage depends on your API quota and billing
- PDF summaries depend on extractable text
- YouTube video must have a public transcript available

  
