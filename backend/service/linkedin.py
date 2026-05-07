# def get_linkedin_profile():
#     return {
#         "name": "Vaishali Arora",
#         "headline": "Solution Architect | PHP | Pimcore",
#         "experience": "14+ years in backend & enterprise systems",
#         "current_role": "Solution Architect at Iksula",
#         "skills": [
#             "PHP",
#             "Symfony",
#             "Pimcore",
#             "MySQL",
#             "AWS",
#             "System Design"
#         ],
#         "linkedin_url": "https://linkedin.com/in/your-profile",
#         "summary": "Experienced Solution Architect specializing in scalable backend systems and enterprise integrations."
#     }

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/get_login")
def get_login():

    
    
    url = (
        f"{os.getenv("LINKEDIN_AUTH_URL")}?response_type=code"
        f"&client_id={os.getenv("CLIENT_ID")}"
        f"&redirect_uri={os.getenv("REDIRECT_URI")}"
        f"&scope=openid%20profile%20email"
        f"&state=random_string_123"
    )

    return url


 
def get_linkedin_profile(code: str = None):
    # Use the saved token from .env if no code is provided
     
    
    headers = {"Authorization": f"Bearer {os.getenv("LINKEDIN_ACCESS_TOKEN")}"}
    response = requests.get("https://api.linkedin.com/v2/userinfo", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        # Fallback to hardcoded data if the token expired
        return {"name": "Vaishali Arora", "note": "Token expired, showing cached data"}