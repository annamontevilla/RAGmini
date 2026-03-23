import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("📄 RAG Document QA System")

# Upload documents
st.header("Upload Documents")
text_input = st.text_area("Paste your documents (separate by ---)")

if st.button("Index Documents"):
    docs = text_input.split("---")
    res = requests.post(f"{API_URL}/upload", json={"texts": docs})
    st.success(res.json())

# Query
st.header("Ask a Question")
query = st.text_input("Your question")

if st.button("Ask"):
    res = requests.post(f"{API_URL}/query", json={"question": query})
    st.write(res.json()["answer"])
