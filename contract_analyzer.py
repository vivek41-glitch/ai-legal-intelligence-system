import pdfplumber
import streamlit as st
from groq import Groq


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def analyze_contract(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert legal contract analyzer."
            },
            {
                "role": "user",
                "content": f"""Analyze this contract and give me:

1. 📋 CONTRACT SUMMARY
2. 🚨 RED FLAGS (dangerous clauses)
3. ✅ KEY CLAUSES
4. ⚠️ MISSING TERMS
5. 💡 RECOMMENDATIONS

Contract:
{text}"""
            }
        ]
    )
    return response.choices[0].message.content

def contract_analyzer_ui():
    st.title("📄 Contract Analyzer")
    st.markdown("Upload any contract PDF and get instant AI analysis.")
    st.markdown("---")

    uploaded_file = st.file_uploader("Upload Contract PDF", type=["pdf"])

    if uploaded_file is not None:
        st.success(f"✅ File uploaded: {uploaded_file.name}")

        if st.button("🔍 Analyze Contract"):
            with st.spinner("Reading and analyzing contract..."):
                text = extract_text_from_pdf(uploaded_file)
                result = analyze_contract(text)

            st.markdown("---")
            st.markdown("## 📊 Analysis Report")
            st.write(result)