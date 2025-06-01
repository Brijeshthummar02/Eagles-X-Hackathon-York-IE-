import requests

class JiraClient:
    def __init__(self, base_url, email, api_token):
        self.base_url = base_url
        self.auth = (email, api_token)
        self.headers = {"Accept": "application/json", "Content-Type": "application/json"}

    def get_issue(self, issue_key):
        url = f"{self.base_url}/rest/api/3/issue/{issue_key}"
        response = requests.get(url, headers=self.headers, auth=self.auth)
        response.raise_for_status()
        issue = response.json()
        summary = issue["fields"]["summary"]

        # Safely extract description text, even if missing or structured differently
        description = ""
        desc_field = issue["fields"].get("description")
        if desc_field and "content" in desc_field and len(desc_field["content"]) > 0:
            content0 = desc_field["content"][0]
            if "content" in content0 and len(content0["content"]) > 0:
                description = content0["content"][0].get("text", "")

        return summary, description

    def transition_issue(self, issue_key, transition_name):
        # Get all transitions available for this issue
        url = f"{self.base_url}/rest/api/3/issue/{issue_key}/transitions"
        response = requests.get(url, headers=self.headers, auth=self.auth)
        response.raise_for_status()
        transitions = response.json().get("transitions", [])

        # Find the transition ID for the name
        transition_id = None
        for t in transitions:
            if t["name"].lower() == transition_name.lower():
                transition_id = t["id"]
                break

        if not transition_id:
            print(f"⚠️ Transition '{transition_name}' not found for {issue_key}.")
            return

        # Perform the transition
        payload = {
            "transition": {
                "id": transition_id
            }
        }
        response = requests.post(url, json=payload, headers=self.headers, auth=self.auth)
        if response.status_code == 204:
            print(f"🔄 Jira issue {issue_key} transitioned to '{transition_name}'.")
        else:
            print(f"❌ Failed to transition issue {issue_key}. Status: {response.status_code}")
