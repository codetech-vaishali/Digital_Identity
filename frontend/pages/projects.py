import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()


st.title(" GitHub Projects")

# username = st.text_input("Enter GitHub Username")


try:
    response = requests.get(
        f"{os.getenv('API_URI')}/githubProjects",
        timeout=5
    )

    if response.status_code == 200:
        data = response.json()

        st.success(f"Total Projects: {data.get('total')}")

        for project in data.get("projects", []):
            st.markdown("---")
            st.subheader(project.get("name"))

            st.write(" Description:", project.get("description"))
            st.write(" Stars:", project.get("stars"))
            st.write(" Language:", project.get("language"))

            st.markdown(f"[🔗 View Repository]({project.get('url')})")

    else:
        st.error("Failed to fetch GitHub data")

except Exception as e:
    st.error(f"Error: {str(e)}")