from dotenv import load_dotenv
import os

load_dotenv()

API_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_PROJECT_DIR = os.path.join(API_ROOT_DIR, "temp")
GITHUB_TEMPLATES_DIR = os.path.join(API_ROOT_DIR, "github", "templates")

"""
If you need to copy the existing project to somewhere new, please use this path below.
If that is not needed, please ignore and just keep the files in temp/ 
"""
DEPLOYMENT_REPOS_DIR = os.path.join(API_ROOT_DIR, "deployments")

# API KEYS
GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")
NETLIFY_API_KEY = os.getenv("NETLIFY_API_KEY")