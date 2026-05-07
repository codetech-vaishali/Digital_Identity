import requests
import os 
from dotenv import load_dotenv

load_dotenv()



def get_github_projects():  
    url=f"{os.getenv("GITHUB_API")}/users/codetech-vaishali/repos"

    try:
        response=requests.get(url,timeout=5)

        if response.status_code !=200:
            return{
                "error":"Failed to fetch data from GitHub",
                "status_code":response.status_code
            }
        
        repos=response.json()

        projects=[]
        for repo in repos:
            projects.append({
                "name":repo.get("name"),
                "description":repo.get("description"),
                "url":repo.get("html_url"),
                "starts":repo.get("stargazers_count"),
                "language":repo.get("language")
            })

        return{
            "total":len(projects),
            "projects":projects
        }  
    except Exception as e:
        return{
            "error":str(e)
        }  
