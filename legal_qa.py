import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from groq import Groq
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
VECTOR_DIR = os.path.join(BASE_DIR, "vectorstore")


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def load_documents():
    docs = []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_DIR, file))
            docs.extend(loader.load())
    return docs

def build_vectorstore():
    with st.spinner("📚 Building knowledge base..."):
        docs = load_documents()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        vectorstore = FAISS.from_documents(chunks, embeddings)
        vectorstore.save_local(VECTOR_DIR)
    return vectorstore

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local(
        VECTOR_DIR, embeddings, allow_dangerous_deserialization=True
    )

def legal_qa_ui():
    st.title("⚖️ Legal Q&A Assistant")
    st.markdown("Ask any legal question based on uploaded law documents.")
    st.markdown("---")

    if "vectorstore" not in st.session_state:
        if os.path.exists(os.path.join(VECTOR_DIR, "index.faiss")):
            with st.spinner("Loading knowledge base..."):
                st.session_state.vectorstore = load_vectorstore()
            st.success("✅ Knowledge base loaded!")
        else:
            st.warning("⚠️ No knowledge base found. Please build it first.")
            if st.button("📚 Build Knowledge Base"):
                st.session_state.vectorstore = build_vectorstore()
                st.success("✅ Done!")

    if "vectorstore" in st.session_state:
        question = st.text_input("💬 Type your legal question here...")
        if st.button("🔍 Get Answer") and question:
            with st.spinner("Analyzing..."):
                docs = st.session_state.vectorstore.similarity_search(question, k=3)
                context = "\n\n".join([doc.page_content for doc in docs])
                response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are an expert Indian legal assistant. Answer clearly using the provided context only."},
                        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
                    ]
                )
            st.markdown("### 📋 Answer")
            st.success(response.choices[0].message.content)
