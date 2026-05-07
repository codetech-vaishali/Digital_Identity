import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.title("My Professional Portfolio")

response = requests.get(f"{os.getenv('API_URI')}/get_linkedin_profile?code=test")

if response.status_code == 200:
    data = response.json()
    

    # Display Data
    st.success("Profile Loaded!")
    st.header(data.get("name"))
    st.subheader(data.get("headline", ""))
    st.write("**Email:**", data.get("email"))
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Experience:**", data.get("experience", "14+ years"))
    with col2:
        st.write("**Current Role:**", data.get("current_role", "Architect"))

    st.markdown("### Skills")
    skills = data.get("skills", ["PHP", "Symfony", "Pimcore"])
    st.write(", ".join(skills))

    if data.get("linkedin_url"):
        st.link_button("View LinkedIn Profile", data.get("linkedin_url"))
