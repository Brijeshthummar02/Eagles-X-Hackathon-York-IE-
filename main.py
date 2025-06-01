import os
from dotenv import load_dotenv
from jira_client import JiraClient
from code_generator import CodeGenerator
from file_writer import FileWriter
from jira_fetcher import fetch_issues, save_issues_as_prompts

def main():
    print("🔁 Loading environment variables...")
    env_loaded = load_dotenv()

    if not env_loaded:
        print("❌ .env file was not found or not loaded properly. Check its location.")

    openai_api_key = os.getenv("OPENAI_API_KEY")
    jira_base_url = os.getenv("JIRA_BASE_URL")
    jira_email = os.getenv("JIRA_EMAIL")
    jira_api_token = os.getenv("JIRA_API_TOKEN")

    print("✅ Env Check:")
    print(f"  OPENAI_API_KEY exists? {'Yes' if openai_api_key else 'No'}")
    print(f"  JIRA_BASE_URL: {jira_base_url}")
    print(f"  JIRA_EMAIL: {jira_email}")
    print(f"  JIRA_API_TOKEN exists? {'Yes' if jira_api_token else 'No'}")

    if not all([openai_api_key, jira_base_url, jira_email, jira_api_token]):
        print("❌ Missing one or more required env variables.")
        return

    try:
        # Always fetch all issues as prompts
        print("📡 Fetching all Jira issues for prompts...")
        issues = fetch_issues()
        save_issues_as_prompts(issues)
        print("✅ Prompt files saved in /prompts/")

        # Ask for single issue key
        issue_key = input("🔑 Enter Jira Issue Key to generate code (e.g., PROJ-123): ").strip()
        if not issue_key:
            print("❌ No issue key provided.")
            return

        print(f"📡 Fetching issue: {issue_key}")
        jira_client = JiraClient(jira_base_url, jira_email, jira_api_token)
        summary, description = jira_client.get_issue(issue_key)

        print("🧠 Generating code...")
        # Set status to "In Progress" in Jira
        jira_client.transition_issue(issue_key, "In Progress")

        code_generator = CodeGenerator(openai_api_key)
        generated_content = code_generator.generate_code(summary, description)

        print("💾 Writing files to 'generated_project/'...")
        file_writer = FileWriter(base_path="generated_project")
        file_writer.write_files(generated_content)

        print("✅ Done! Check the 'generated_project' folder.")

    except Exception as e:
        print(f"❗ Error: {e}")

if __name__ == "__main__":
    main()
