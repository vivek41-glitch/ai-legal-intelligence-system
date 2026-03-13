import os
from groq import Groq
import streamlit as st

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def predict_case(case_type, your_side, opponent_side, evidence, location):
    prompt = f"""You are an expert Indian legal advisor with 20 years of experience in Indian courts.
Analyze the following legal case and provide a detailed prediction and guidance.

Case Type: {case_type}
Location: {location}

My Side of the Story:
{your_side}

Opponent's Side:
{opponent_side}

Evidence Available:
{evidence}

Please provide a detailed analysis in the following format:

⚖️ CASE ASSESSMENT
[Identify the type of case, applicable Indian laws and sections]

📊 OUTCOME PREDICTION
[Predict likelihood of winning/losing with percentage and clear reasoning]

✅ STRENGTHS IN YOUR CASE
[List all factors that are in the user's favor]

🚨 WEAKNESSES IN YOUR CASE
[List all factors that could go against the user]

💡 RECOMMENDED NEXT STEPS
[Step by step guidance on what to do next]

⏱️ TIME AND COST ESTIMATE
[Typical duration and approximate legal costs for this type of case in India]

⚠️ IMPORTANT DISCLAIMER
[Add legal disclaimer]"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert Indian legal advisor. Always provide detailed, accurate analysis based on Indian law. Always include a disclaimer that this is AI-generated advice and not a substitute for professional legal counsel."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3000
    )
    return response.choices[0].message.content

def case_predictor_ui():
    st.title("🔮 Case Outcome Predictor")
    st.markdown("Describe your legal situation and get an AI-powered case analysis.")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        case_type = st.selectbox("Select Case Type", [
            "Property Dispute",
            "Employment / Labour Dispute",
            "Consumer Complaint",
            "Family / Divorce Matter",
            "Criminal Case",
            "Contract Breach",
            "Cybercrime",
            "Cheque Bounce (NI Act)",
            "Rent Dispute",
            "Other"
        ])

    with col2:
        location = st.text_input("Your State / City", placeholder="e.g. Mumbai, Maharashtra")

    st.markdown("### 📝 Describe Your Case")

    your_side = st.text_area(
        "Your Side of the Story",
        placeholder="Describe what happened from your perspective in detail...",
        height=150
    )

    opponent_side = st.text_area(
        "Opponent's Side (if known)",
        placeholder="What is the other party claiming or arguing?",
        height=100
    )

    evidence = st.text_area(
        "Evidence You Have",
        placeholder="List any evidence you have: documents, photos, witnesses, receipts, contracts, messages etc.",
        height=100
    )

    st.markdown("---")

    if st.button("🔮 Predict Case Outcome"):
        if not your_side:
            st.warning("⚠️ Please describe your side of the story first!")
        elif not location:
            st.warning("⚠️ Please enter your location!")
        else:
            with st.spinner("Analyzing your case under Indian law..."):
                prediction = predict_case(
                    case_type, your_side, opponent_side, evidence, location
                )

            st.markdown("---")
            st.markdown("## 📊 Case Analysis Report")
            st.markdown(prediction)

            st.markdown("---")
            st.info("⚠️ This analysis is AI-generated and should not be treated as professional legal advice. Please consult a qualified lawyer for your specific situation.")

            st.download_button(
                label="📥 Download Report",
                data=prediction,
                file_name="case_analysis_report.txt",
                mime="text/plain"
            )