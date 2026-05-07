from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse

from fastapi.middleware.cors import CORSMiddleware

from backend.service.github import get_github_projects
from backend.service.linkedin import get_login
from backend.service.linkedin import get_linkedin_profile


app=FastAPI(title="Portfolio API")

app.add_middleware(CORSMiddleware,
                    allow_origins=["*"],
                    allow_methods=["*"], 
                    allow_headers=["*"])

@app.get("/")
def root():
    return {"message": "Welcome to the Portfolio API"}

@app.get("/login")
def login():
    # We get the URL from the service and tell the browser to GO there
    target_url = get_login()
    return RedirectResponse(url=target_url)
    

@app.get("/get_linkedin_profile")
def linkedin_callback(code: str= None,error:str = None):
    if error:
        return {"error": error}
    if not code:
        return {"error": "No code provided"}
    
    
    return get_linkedin_profile(code)

@app.get("/githubProjects")
def github_projects():
    return get_github_projects()

