from fastapi import FastAPI
from pydantic import BaseModel
from rag import RAGSystem
from openai import OpenAI

app = FastAPI()
rag = RAGSystem()
client = OpenAI(api_key="add_your_key")

class DocumentRequest(BaseModel):
    texts: list[str]

class QueryRequest(BaseModel):
    question: str

@app.post("/upload")
def upload_docs(req: DocumentRequest):
    rag.add_documents(req.texts)
    return {"status": "Documents indexed"}

@app.post("/query")
def query(req: QueryRequest):
    context_chunks = rag.query(req.question)
    context = "\n".join(context_chunks)

    prompt = f"""
    Answer using ONLY this context:
    {context}

    Question: {req.question}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"answer": response.choices[0].message.content}