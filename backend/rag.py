import faiss
import numpy as np
from embeddings import embed_text

class RAGSystem:
    def __init__(self):
        self.chunks = []
        self.index = None

    def add_documents(self, texts):
        self.chunks = texts
        embeddings = embed_text(texts)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings))

    def query(self, question, k=3):
        query_vec = embed_text([question])
        D, I = self.index.search(np.array(query_vec), k)
        return [self.chunks[i] for i in I[0]]