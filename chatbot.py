# chatbot.py
import os
import requests
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv("API_URL")
HF_API_KEY = os.getenv("HF_API_KEY")
MODEL = os.getenv("MODEL")

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def load_documents():
    pdf_loader = PyPDFLoader("resume.pdf")
    txt_loader = TextLoader("data.txt")
    return pdf_loader.load() + txt_loader.load()

def create_vector_store(docs):
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(split_docs, embeddings)
    return db

def query_huggingface(prompt, context=[]):
    context_str = "\n\n".join(context)
    full_prompt = (
        f"You are MD Mazul Haque. Answer the question using only the information in the context. "
        f"Respond in first person, like you are talking about yourself.\n\n"
        f"Context:\n{context_str}\n\n"
        f"Question: {prompt}"
    )
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": full_prompt}]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"API Error: {response.status_code} - {response.text}"

class MyChatBot:
    def __init__(self):
        print(" Loading documents...")
        docs = load_documents()
        print(" Creating FAISS index...")
        self.db = create_vector_store(docs)
        print(" Bot ready!")

    def ask(self, query):
        context_docs = self.db.similarity_search(query, k=3)
        context = [doc.page_content for doc in context_docs]
        return query_huggingface(query, context)
