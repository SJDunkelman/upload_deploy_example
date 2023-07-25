import requests
import re
import config


github_repo = "sjdunkelman/client_name_landing_page_4a7383f3-b8eb-41ee-86ac-db3458bf24c0"
access_token = config.VERCEL_API_KEY


def create_vercel_project(access_token, github_repo):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # name = re.search(r'/([^/]*)$', github_repo).group(1)
    # name = name.replace('_', '-').lower()
    # name = re.sub(r'/[^A-Za-z0-9-]+/g', '', name)
    data = {
        "name": "my-test-website",  # Set your desired project name here
        "gitRepository": {
            "repo": github_repo,
            "type": 'github',
            "sourceless": True
        },
        "framework": "astro"  # Set the framework to "astro" for Astro JS projects
    }

    response = requests.post("https://api.vercel.com/v6/projects", headers=headers, json=data)
    return response.json()


def deploy_vercel_project(access_token, project_id):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    body = {
        "branch": {
            "id": "SOME_STRING_VALUE",
            "project_id": "prj_Eqi8JqvZ2Xt1QbiiW2GALkf1np34",
            "name": "my-test-website",
            "current_state": "init",
            "primary": True
        }
    }

    response = requests.post(f"https://api.vercel.com/v1/projects/{project_id}/deployments",data=body, headers=headers)
    return response.json()


if __name__ == "__main__":
    # Replace with your actual Vercel access token and GitHub repository URL
    vercel_access_token = config.VERCEL_API_KEY
    github_repo_url = "sjdunkelman/client_name_landing_page_4a7383f3-b8eb-41ee-86ac-db3458bf24c0"

    # Step 1: Create the Vercel project
    project_data = create_vercel_project(vercel_access_token, github_repo_url)
    project_id = project_data["id"]
    print(f"Vercel project created! Project ID: {project_id}")

    # Step 2: Deploy the project
    deploy_data = deploy_vercel_project(vercel_access_token, project_id)
    deployment_url = deploy_data["url"]
    print(f"Vercel project deployed! Deployment URL: {deployment_url}")
