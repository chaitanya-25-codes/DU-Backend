# DU-Backend

## 🔧 Overview
**DU-Backend** is an AI-powered document ingestion and analysis backend built with FastAPI. It accepts document uploads (PDF, TXT, DOCX), extracts and chunks text, generates embeddings, stores vectors in Chroma, and performs retrieval-augmented generation (RAG) or general summarization using OpenAI models.

---

## ✅ Implemented Features
- **File upload endpoint:** `POST /api/submit` — accepts `file` and `description` (form data). Saves uploaded files to `uploads/` and returns a JSON response with the LLM output.
- **Text extraction:** Uses `pdfplumber` for PDFs, `python-docx` for `.docx`, and plain text reading for `.txt`.
- **Chunking:** Uses `RecursiveCharacterTextSplitter` (chunk size 800, overlap 100) to split long texts for embedding/search.
- **Embeddings & Vector DB:** Uses OpenAI embeddings (`text-embedding-3-small`) via `langchain_openai` and stores vectors with Chroma in `chroma-db/` (persisted).
- **Intent detection:** A small LLM prompt classifies the user `description` into `GENERAL_SUMMARY` or `PURPOSE_DRIVEN_ANALYSIS` and chooses the RAG path accordingly.
- **RAG flow:** For purpose-driven requests, performs similarity search (k=5) and crafts a prompt including context, then generates a response with `ChatOpenAI` (models used: `gpt-4o-mini`, `gpt-4o-mini`/`gpt-4o-mini` variants configured in code).
- **Simple, extensible design:** Clearly separated services in `app/services/` (`parser`, `chunker`, `chroma`, `intent`, `rag`) and a route in `app/routes/upload.py`.

---

## 🧰 Packages / Dependencies
The primary dependencies are (see `requirements.txt`):

```
fastapi
uvicorn
pydantic
python-dotenv
python-multipart

# Document parsing
pdfplumber
python-docx

# AI & embeddings
openai
langchain
langchain-community
langchain-openai
chromadb
tiktoken
httpx
```

---

## ⚙️ Setup
1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Add a `.env` file with your OpenAI key:

```
OPENAI_API_KEY=sk-...
```

3. Make sure the following folders exist (they are created automatically by the app but verify if needed):
- `uploads/` (uploaded files)
- `chroma-db/` (Chroma persistence)

---

## ▶️ Run the app

```bash
uvicorn app.main:app --reload --port 8000
```
Open the API docs at `http://localhost:8000/docs`.

---

## 🔌 Usage example
Upload a file and a short description that expresses intent:

```bash
curl -X POST "http://localhost:8000/api/submit" \
  -F "file=@/path/to/doc.pdf" \
  -F "description=Summarize the key points and extract action items"
```
Response includes `filename`, `doc_id`, `description`, and `llm_response` with the generated summary/analysis.

---

## 🗂️ Data & Persistence
- Uploaded files are stored in `uploads/`.
- Chroma persists embeddings and related files in `chroma-db/`.
- New collections are created per `doc_id` when a document is submitted.

---

## 💡 Notes & Caveats
- Make sure your OpenAI API key has access to the models you plan to use. Requests to LLMs and embedding APIs will generate usage costs.
- Large documents are chunked but very large inputs may still hit rate/size limits — tune chunk size or process in batches as needed.
- The repo is structured for easy extension (add more routes, improve prompts or add caching).

---

If you'd like, I can also add an example Postman collection or a small Python client script to make testing the `/api/submit` endpoint easier. ✅