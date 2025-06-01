import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT_KEY = "WEAT"

AUTH = (JIRA_EMAIL, JIRA_API_TOKEN)
HEADERS = {"Accept": "application/json"}

def fetch_issues():
    if not JIRA_BASE_URL:
        raise ValueError("Missing JIRA_BASE_URL from environment.")

    jql = f"project={JIRA_PROJECT_KEY}"
    url = f"{JIRA_BASE_URL}/rest/api/3/search"
    params = {"jql": jql, "maxResults": 100}

    response = requests.get(url, headers=HEADERS, auth=AUTH, params=params)
    response.raise_for_status()

    issues = response.json()["issues"]
    return issues

def save_issues_as_prompts(issues):
    os.makedirs("prompts", exist_ok=True)

    for issue in issues:
        key = issue["key"]
        summary = issue["fields"]["summary"]
        description_field = issue["fields"].get("description")

        # Parse rich text format (if present)
        if description_field and isinstance(description_field, dict):
            desc_text = ""
            for block in description_field.get("content", []):
                for p in block.get("content", []):
                    desc_text += p.get("text", "") + "\n"
        else:
            desc_text = str(description_field or "")

        content = f"Issue: {key}\nTitle: {summary}\n\nDescription:\n{desc_text}"
        with open(f"prompts/{key}.txt", "w", encoding="utf-8") as f:
            f.write(content)

    print(f"✅ Saved {len(issues)} prompt files to /prompts")
