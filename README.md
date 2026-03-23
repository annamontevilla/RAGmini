# RAGmini
Small RAG Project
## Features
- Semantic search using embeddings
- FAISS vector database
- LLM-based answers
- FastAPI backend
- Streamlit frontend

## Run Backend
cd backend
pip install -r requirements.txt
uvicorn app:app --reload

## Run Frontend
cd frontend
pip install -r requirements.txt
streamlit run app.py

## Usage
1. Paste documents
2. Index them
3. Ask questions

## Future Improvements
- PDF ingestion
- Persistent vector DB
- Authentication
- Docker support
