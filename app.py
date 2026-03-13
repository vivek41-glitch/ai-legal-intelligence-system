
import streamlit as st

st.set_page_config(
    page_title="AI Legal Intelligence System",
    page_icon="⚖️",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0a0f1e;
    color: #e8e0d0;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px !important;
}

.header-bar {
    background: linear-gradient(135deg, #0d1b2a 0%, #1a2f4e 50%, #0d1b2a 100%);
    border-bottom: 2px solid #c9a84c;
    padding: 22px 40px;
    margin: -1rem -1rem 2rem -1rem;
    text-align: center;
}
.header-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: #c9a84c;
    letter-spacing: 1px;
}
.header-subtitle {
    font-size: 0.78rem;
    color: #8a9bb5;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 4px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    color: #c9a84c;
    font-weight: 700;
    margin-bottom: 0.3rem;
}
.section-divider {
    height: 2px;
    background: linear-gradient(90deg, #c9a84c, transparent);
    margin-bottom: 1.5rem;
    border-radius: 2px;
}

.stat-card {
    background: linear-gradient(135deg, #0d1b2a, #1a2f4e);
    border: 1px solid #1e3a5f;
    border-top: 3px solid #c9a84c;
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    height: 180px;
    transition: transform 0.2s;
}
.stat-card:hover { transform: translateY(-3px); }
.stat-icon { font-size: 2.2rem; margin-bottom: 10px; }
.stat-title {
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    color: #c9a84c;
    font-weight: 600;
    margin-bottom: 6px;
}
.stat-desc { font-size: 0.78rem; color: #6b7f99; line-height: 1.5; }

/* NAV BUTTONS - equal size */
div[data-testid="column"] .stButton > button {
    background: #0d1b2a !important;
    border: 1px solid #c9a84c !important;
    color: #c9a84c !important;
    border-radius: 10px !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    width: 100% !important;
    height: 50px !important;
    white-space: normal !important;
    line-height: 1.2 !important;
}
div[data-testid="column"] .stButton > button:hover {
    background: #c9a84c !important;
    color: #0a0f1e !important;
}

/* ALL OTHER BUTTONS */
.stButton > button {
    background: linear-gradient(135deg, #c9a84c, #e8c96d) !important;
    color: #0a0f1e !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 10px 28px !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    width: 100% !important;
}
.stButton > button:hover {
    box-shadow: 0 4px 15px rgba(201,168,76,0.4) !important;
}

/* INPUT LABELS */
.stTextInput > label,
.stTextArea > label,
.stSelectbox > label,
.stDateInput > label {
    color: #c9a84c !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
}

/* INPUT BOXES - white background, black text, visible */
.stTextInput > div > div > input {
    background-color: #ffffff !important;
    border: 1px solid #c9a84c !important;
    border-radius: 8px !important;
    color: #000000 !important;
    font-size: 0.9rem !important;
    padding: 10px !important;
}
.stTextArea > div > div > textarea {
    background-color: #ffffff !important;
    border: 1px solid #c9a84c !important;
    border-radius: 8px !important;
    color: #000000 !important;
    font-size: 0.9rem !important;
    padding: 10px !important;
}
.stSelectbox > div > div {
    background-color: #ffffff !important;
    border: 1px solid #c9a84c !important;
    border-radius: 8px !important;
    color: #000000 !important;
}
input::placeholder, textarea::placeholder {
    color: #999999 !important;
}

.stFileUploader > div {
    background: #0d1b2a !important;
    border: 2px dashed #c9a84c !important;
    border-radius: 12px !important;
}

.law-footer {
    text-align: center;
    padding: 20px;
    color: #3a4f6b;
    font-size: 0.72rem;
    border-top: 1px solid #1e3a5f;
    margin-top: 3rem;
    letter-spacing: 1.5px;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="header-bar">
    <div class="header-title">⚖️ AI Legal Intelligence System</div>
    <div class="header-subtitle">Your Smart Legal Companion for Indian Law</div>
</div>
""", unsafe_allow_html=True)

# NAV
if "page" not in st.session_state:
    st.session_state.page = "Home"

c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])
with c1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
with c2:
    if st.button("📖 Legal Q&A"):
        st.session_state.page = "Legal Q&A"
with c3:
    if st.button("📄 Contracts"):
        st.session_state.page = "Contract Analyzer"
with c4:
    if st.button("📝 Documents"):
        st.session_state.page = "Document Generator"
with c5:
    if st.button("🔮 Predictor"):
        st.session_state.page = "Case Predictor"

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

page = st.session_state.page

if page == "Home":
    st.markdown('<div class="section-title">Welcome to AI Legal Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("##### Instant legal guidance powered by AI — accessible to everyone, anywhere in India.")
    st.markdown("")

    c1, c2, c3, c4 = st.columns(4)
    cards = [
        ("📖", "Legal Q&A", "Ask any legal question from our knowledge base of Indian law documents."),
        ("📄", "Contract Analyzer", "Upload any contract and get instant clause-by-clause risk analysis."),
        ("📝", "Document Generator", "Generate NDAs, rental agreements, employment contracts instantly."),
        ("🔮", "Case Predictor", "Describe your situation and get AI-powered legal outcome prediction.")
    ]
    for col, (icon, title, desc) in zip([c1, c2, c3, c4], cards):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">{icon}</div>
                <div class="stat-title">{title}</div>
                <div class="stat-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #0d1b2a, #1a2f4e);
                border: 1px solid #1e3a5f; border-left: 4px solid #c9a84c;
                border-radius: 12px; padding: 20px; margin-top: 1.5rem;">
        <span style="color:#c9a84c; font-weight:600;">⚠️ Disclaimer: </span>
        <span style="color:#8a9bb5; font-size:0.85rem;">
        This system provides AI-generated legal information for educational purposes only.
        It is not a substitute for professional legal advice. Always consult a qualified lawyer.
        </span>
    </div>
    """, unsafe_allow_html=True)

elif page == "Legal Q&A":
    st.markdown('<div class="section-title">📖 Legal Q&A Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    from legal_qa import legal_qa_ui
    legal_qa_ui()

elif page == "Contract Analyzer":
    st.markdown('<div class="section-title">📄 Contract Analyzer</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    from contract_analyzer import contract_analyzer_ui
    contract_analyzer_ui()

elif page == "Document Generator":
    st.markdown('<div class="section-title">📝 Legal Document Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    from doc_generator import doc_generator_ui
    doc_generator_ui()

elif page == "Case Predictor":
    st.markdown('<div class="section-title">🔮 Case Outcome Predictor</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    from case_predictor import case_predictor_ui
    case_predictor_ui()

st.markdown("""
<div class="law-footer">
    AI LEGAL INTELLIGENCE SYSTEM &nbsp;|&nbsp; FOR EDUCATIONAL USE ONLY &nbsp;|&nbsp; NOT A SUBSTITUTE FOR LEGAL ADVICE
</div>
""", unsafe_allow_html=True)