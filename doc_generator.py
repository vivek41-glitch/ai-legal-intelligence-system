import os
from groq import Groq
import streamlit as st
from fpdf import FPDF
import tempfile


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_document(doc_type, fields):
    prompt = f"""You are an expert Indian legal document drafter.
Generate a complete, professional and legally valid {doc_type} using the details below.
Use proper legal language, numbering, and formatting.
Include all standard clauses required for this type of document in India.

Details provided:
{fields}

Generate the complete document now:"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert Indian legal document drafter. Always generate complete, professional legal documents."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3000
    )
    return response.choices[0].message.content

def save_as_pdf(text, filename="legal_document.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    pdf.set_margins(20, 20, 20)
    for line in text.split('\n'):
        pdf.multi_cell(0, 8, txt=line.encode('latin-1', 'replace').decode('latin-1'))
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(tmp.name)
    return tmp.name

def doc_generator_ui():
    st.title("📝 Legal Document Generator")
    st.markdown("Fill the form below to generate a professional legal document.")
    st.markdown("---")

    doc_type = st.selectbox("Select Document Type", [
        "Rental Agreement",
        "Non Disclosure Agreement (NDA)",
        "Employment Contract",
        "Partnership Agreement",
        "Service Agreement"
    ])

    st.markdown("### 📋 Fill Document Details")

    fields = ""

    if doc_type == "Rental Agreement":
        col1, col2 = st.columns(2)
        with col1:
            landlord = st.text_input("Landlord Full Name")
            tenant = st.text_input("Tenant Full Name")
            rent = st.text_input("Monthly Rent (INR)")
            duration = st.text_input("Duration (e.g. 11 months)")
        with col2:
            address = st.text_input("Property Address")
            start_date = st.date_input("Start Date")
            deposit = st.text_input("Security Deposit (INR)")
            city = st.text_input("City")
        fields = f"""
        Landlord: {landlord}
        Tenant: {tenant}
        Property Address: {address}
        Monthly Rent: INR {rent}
        Security Deposit: INR {deposit}
        Duration: {duration}
        Start Date: {start_date}
        City: {city}
        """

    elif doc_type == "Non Disclosure Agreement (NDA)":
        col1, col2 = st.columns(2)
        with col1:
            party1 = st.text_input("Disclosing Party Name")
            party2 = st.text_input("Receiving Party Name")
            purpose = st.text_input("Purpose of NDA")
        with col2:
            duration = st.text_input("NDA Duration (e.g. 2 years)")
            city = st.text_input("City")
            date = st.date_input("Agreement Date")
        fields = f"""
        Disclosing Party: {party1}
        Receiving Party: {party2}
        Purpose: {purpose}
        Duration: {duration}
        City: {city}
        Date: {date}
        """

    elif doc_type == "Employment Contract":
        col1, col2 = st.columns(2)
        with col1:
            employer = st.text_input("Employer / Company Name")
            employee = st.text_input("Employee Full Name")
            role = st.text_input("Job Title / Role")
            salary = st.text_input("Monthly Salary (INR)")
        with col2:
            start_date = st.date_input("Joining Date")
            location = st.text_input("Work Location")
            notice = st.text_input("Notice Period (e.g. 30 days)")
            city = st.text_input("City")
        fields = f"""
        Employer: {employer}
        Employee: {employee}
        Role: {role}
        Salary: INR {salary}
        Joining Date: {start_date}
        Work Location: {location}
        Notice Period: {notice}
        City: {city}
        """

    elif doc_type == "Partnership Agreement":
        col1, col2 = st.columns(2)
        with col1:
            partner1 = st.text_input("Partner 1 Full Name")
            partner2 = st.text_input("Partner 2 Full Name")
            business = st.text_input("Business Name")
            share1 = st.text_input("Partner 1 Share %")
        with col2:
            share2 = st.text_input("Partner 2 Share %")
            capital = st.text_input("Total Capital (INR)")
            city = st.text_input("City")
            date = st.date_input("Agreement Date")
        fields = f"""
        Partner 1: {partner1}
        Partner 2: {partner2}
        Business Name: {business}
        Partner 1 Share: {share1}%
        Partner 2 Share: {share2}%
        Total Capital: INR {capital}
        City: {city}
        Date: {date}
        """

    elif doc_type == "Service Agreement":
        col1, col2 = st.columns(2)
        with col1:
            provider = st.text_input("Service Provider Name")
            client_name = st.text_input("Client Name")
            service = st.text_input("Service Description")
            amount = st.text_input("Service Amount (INR)")
        with col2:
            duration = st.text_input("Duration")
            start_date = st.date_input("Start Date")
            city = st.text_input("City")
            payment = st.text_input("Payment Terms")
        fields = f"""
        Service Provider: {provider}
        Client: {client_name}
        Service: {service}
        Amount: INR {amount}
        Duration: {duration}
        Start Date: {start_date}
        City: {city}
        Payment Terms: {payment}
        """

    st.markdown("---")
    if st.button("⚡ Generate Document"):
        if not any(fields.split()):
            st.warning("⚠️ Please fill in the details first!")
        else:
            with st.spinner("Generating your legal document..."):
                document = generate_document(doc_type, fields)
            st.markdown("### 📄 Generated Document")
            st.text_area("", document, height=500)
            pdf_path = save_as_pdf(document)
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📥 Download as PDF",
                    data=f,
                    file_name=f"{doc_type.replace(' ', '_')}.pdf",
                    mime="application/pdf"
                )