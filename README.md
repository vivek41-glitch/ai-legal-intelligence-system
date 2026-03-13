# ⚖️ AI Legal Intelligence System

A production-ready AI-powered legal assistant for Indian law built with RAG, LangChain, FAISS, and Groq.

## 🌐 Live Demo
[Click here to try the live app](https://ai-legal-intelligence-system-ftcsqsyljmhonks5ka4xk2.streamlit.app)

## 🚀 Features

### 📖 Phase 1 — Legal Q&A (RAG)
- Ask any legal question based on uploaded Indian law documents
- Powered by FAISS vector database + HuggingFace embeddings
- Retrieval Augmented Generation (RAG) pipeline

### 📄 Phase 2 — Contract Analyzer
- Upload any contract PDF
- AI analyzes red flags, key clauses, missing terms
- Powered by Groq + Llama 3.3

### 📝 Phase 3 — Legal Document Generator
- Generate NDAs, Rental Agreements, Employment Contracts
- Partnership Agreements, Service Agreements
- Download as PDF instantly

### 🔮 Phase 4 — Case Outcome Predictor
- Describe your legal situation
- Get AI-powered outcome prediction
- Applicable Indian laws, strengths, weaknesses, next steps

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Core language |
| Streamlit | Frontend UI |
| LangChain | RAG pipeline |
| FAISS | Vector database |
| HuggingFace | Embeddings |
| Groq + Llama 3.3 | LLM inference |
| pdfplumber | PDF extraction |
| fpdf | PDF generation |

## ⚙️ Run Locally

1. Clone the repository
```
git clone https://github.com/vivek41-glitch/ai-legal-intelligence-system.git
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Create `.env` file
```
GROQ_API_KEY=your_groq_key_here
HUGGINGFACE_API_KEY=your_hf_key_here
```

4. Run the app
```
streamlit run app.py
```

## 📁 Project Structure
```
ai-legal-intelligence-system/
│
├── app.py                  ← Main entry point
├── legal_qa.py             ← Phase 1: Legal Q&A
├── contract_analyzer.py    ← Phase 2: Contract Analyzer  
├── doc_generator.py        ← Phase 3: Document Generator
├── case_predictor.py       ← Phase 4: Case Predictor
├── data/                   ← Legal PDF documents
├── vectorstore/            ← FAISS vector database
└── requirements.txt        ← Dependencies
```

## ⚠️ Disclaimer
This system provides AI-generated legal information for educational purposes only.
It is not a substitute for professional legal advice.

## 👨‍💻 Built By
**Vivek Dubey** —  AI/ML Developer

```