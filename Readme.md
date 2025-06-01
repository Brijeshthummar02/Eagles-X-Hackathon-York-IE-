**⚡ CODESTORM** - *From Jira Ticket to Deployed Code in One Command*
====================================================================

🏆 *Built in 12 Hours - Our First Hackathon Masterpiece* 🏆
-----------------------------------------------------------

**Hackathon Problem Statement**
-------------------------------

Revolutionize the software development lifecycle by creating an AI-powered assistant that automates workflows from Jira task to production-ready code---seamlessly integrating planning, coding, testing, and deployment. Your goal: Build an intelligent system within Void Editor that eliminates manual toil, reduces context-switching, and accelerates delivery---while maintaining high standards of quality.

**The Challenge: Autonomous Jira-to-Code Pipeline**
---------------------------------------------------

Our solution creates a complete end-to-end automation system that transforms Jira tickets into production-ready code with minimal human intervention.

**12-Hours Hackathon!**
----------------------------------------------

* * * * *

🎯 **What We Built**
--------------------

An intelligent automation pipeline that:

-   Fetches Jira tickets automatically using OAuth Atlassian integration
-   Generates complete, production-ready code using OpenAI LLM
-   Updates Jira ticket status in real-time
-   Tests and iterates code based on user feedback
-   Automatically pushes to GitHub
-   Manages project lifecycle from "To Do" to "Done"

🔧 **Prerequisites**
--------------------

-   Python 3.7+ installed
-   OpenAI API Key
-   Jira Base URL
-   Jira Email Address
-   Jira API Token
-   GitHub credentials (for deployment)

📦 **Installation**
-------------------

bash

```
$ pip install openai requests python-dotenv
```

⚙️ **Setup**
------------

1.  Create a `.env` file in your project root:

env

```
OPENAI_API_KEY=your_openai_api_key
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@domain.com
JIRA_API_TOKEN=your_jira_api_token
```

1.  Ensure your Jira account has proper permissions
2.  Set up GitHub authentication for automatic deployment

🏃‍♂️ **How to Run**
--------------------

bash

```
$ python main.py
```

📋 **Workflow Process**
-----------------------

### 1\. **Ticket Fetching**

-   Connects to Jira using OAuth 2.0 authentication
-   Fetches all available tickets from your Jira workspace
-   Saves ticket details as prompt files in `/prompts` folder

### 2\. **Code Generation**

-   User selects specific Jira ticket by entering issue key
-   System reads ticket requirements from saved prompt file
-   OpenAI LLM generates complete project structure and code
-   Automatically transitions Jira ticket from "To Do" to "In Progress"

### 3\. **Testing & Iteration**

-   Generated code is automatically tested
-   User gets option to keep code or enhance it
-   System iterates in a loop until user confirms satisfaction
-   Continuous improvement through AI feedback loop

### 4\. **Deployment**

-   User gets option to push code to GitHub
-   For personal repositories: Jira ticket automatically moves to "Done"
-   For organization/open source repos: Ticket updates after code merge
-   Zero manual intervention required

💻 **Sample Execution**
-----------------------

bash

```
brije@Brijesh MINGW64 ~/Desktop/Eagles x hackathon
$ python main.py
🔁 Loading environment variables...
✅ Env Check:
  OPENAI_API_KEY exists? Yes
  JIRA_BASE_URL: https://yorkhackathonteam1.atlassian.net
  JIRA_EMAIL: yorkhackathonteam1@gmail.com
  JIRA_API_TOKEN exists? Yes
📡 Fetching all Jira issues for prompts...
✅ Saved 5 prompt files to /prompts
✅ Prompt files saved in /prompts/
🔑 Enter Jira Issue Key to generate code (e.g., PROJ-123): WEAT-4
📡 Fetching issue: WEAT-4
🧠 Generating code...
🔄 Jira issue WEAT-4 transitioned to 'In Progress'.
💾 Writing files to 'generated_project/'...
✅ Created: generated_project\package.json
✅ Created: generated_project\vite.config.ts
✅ Created: generated_project\tsconfig.json
✅ Created: generated_project\tailwind.config.js
✅ Created: generated_project\postcss.config.js
✅ Created: generated_project\public/index.html
✅ Created: generated_project\src/main.tsx
✅ Created: generated_project\src/App.tsx
✅ Created: generated_project\src/pages/HomePage.tsx
✅ Created: generated_project\src/components/custom/WeatherDisplay.tsx
✅ Created: generated_project\src/hooks/useWeatherStore.ts
📁 Project written to: generated_project
✅ Done! Check the 'generated_project' folder.
```

🌟 **Key Features**
-------------------

-   **🔄 Automated Workflow**: Complete automation from Jira ticket to deployed code
-   **🤖 AI-Powered**: Leverages OpenAI LLM for intelligent code generation
-   **📊 Real-time Updates**: Synchronizes Jira ticket status automatically
-   **🔧 Iterative Enhancement**: Continuous code improvement through AI feedback
-   **🚀 One-Click Deployment**: Direct GitHub integration for seamless deployment
-   **📁 Organized Output**: Structured project generation with proper file hierarchy

🛠️ **Technical Stack**
-----------------------

-   **Backend**: Python
-   **AI/ML**: OpenAI GPT API
-   **Project Management**: Jira REST API
-   **Version Control**: GitHub API
-   **Authentication**: OAuth 2.0 (Atlassian)
-   **Environment Management**: python-dotenv

👥 **Team**
-----------

First-time hackathon participants who transformed an ambitious idea into a working solution in record time!

🎉 **Impact**
-------------

This solution eliminates:

-   Manual context-switching between tools
-   Time-consuming code setup and boilerplate generation
-   Manual Jira ticket status updates
-   Deployment pipeline configuration
-   Code review bottlenecks for standard implementations

* * * * *

*"Every expert was once a beginner. Every pro was once an amateur."* 🔥