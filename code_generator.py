import openai
import os

class CodeGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_code(self, summary, description):
        prompt = (
            "You are a Senior Full-Stack Developer with a strong specialization in modern UI/UX, frontend architecture, and rapid prototyping. "
            "Your task is to generate a complete, runnable codebase for a web application based on the provided Jira ticket details. "
            "The primary emphasis of this project is on outstanding visual design and user experience, leveraging cutting-edge UI libraries and a modern tech stack.\n\n"

            f"Jira Ticket Details (to be provided when this prompt is used):\n"
            f"Title: {summary}\n"
            f"Description: {description}\n\n"

            "Core Mandate: Design-First & Runnable Output\n"
            "The main functionality and effort must be dedicated to creating a visually stunning, intuitive, and responsive user interface. "
            "While the backend might be mocked or minimal, the frontend presentation must be polished and professional. "
            "Critically, the generated codebase must be complete and correctly configured such that after running npm install (or yarn install) followed by npm run dev (or yarn dev/npm start), the application starts successfully without errors.\n\n"

            "Technical Stack & Library Requirements:\n\n"
            "1. Core Framework: React with TypeScript.\n"
            "2. Build Tool: Vite (preferred for speed and modern setup) or Create React App.\n"
            "3. Styling:\n"
            "   * Tailwind CSS as the foundational styling utility.\n"
            "   * Integrate one of the following (or comparable) modern UI component libraries:\n"
            "     - Shadcn/UI (preferred if applicable, ensure components.json and CLI setup is conceptually represented or explained if direct CLI simulation isn't possible)\n"
            "     - Aceternity UI\n"
            "     - Skeleton UI\n"
            "   * The chosen library must be properly set up with Tailwind CSS. This includes any necessary Tailwind plugins or configurations (e.g., for Shadcn/UI theme variables, animations).\n"
            "4. State Management (if needed): Zustand, Jotai, or React Context API (avoid Redux).\n"
            "5. Routing (if needed): React Router DOM.\n\n"

            "Project Structure & Deliverables:\n\n"
            "1. package.json:\n"
            "   * All necessary dependencies for React, ReactDOM, TypeScript, Tailwind CSS, UI library, PostCSS, Autoprefixer, Vite/CRA, and any other chosen libraries (e.g., React Router DOM, state management).\n"
            "   * Scripts: A working dev (or start) script to launch the development server, and a build script.\n"
            "2. tsconfig.json: Appropriately configured for a React TypeScript project with Vite/CRA.\n"
            "3. vite.config.ts (if using Vite) or relevant CRA configuration files.\n"
            "4. tailwind.config.js and postcss.config.js: Correctly set up for Tailwind CSS, including content paths and any UI library-specific configurations.\n"
            "5. public/index.html with root div and basic meta tags.\n"
            "6. src/ folder containing:\n"
            "   - main.tsx (for Vite) or index.tsx (for CRA)\n"
            "   - App.tsx (main application component)\n"
            "   - styles/globals.css or assets/css/index.css → global styles, including Tailwind base/components/utilities imports.\n"
            "   - components/ui/ (if using Shadcn/UI, for library components) and components/custom/ → 2–3 polished custom components, potentially utilizing the chosen UI library.\n"
            "   - pages/ or views/, if multiple views are implied by the Jira ticket.\n"
            "   - layouts/, lib/ (e.g., cn utility for Shadcn), hooks/, as needed.\n\n"

            "Visual Polish:\n"
            "* Thoughtful typography, consistent spacing, and a modern, appealing color palette.\n"
            "* Fully responsive design, adapting gracefully to different screen sizes.\n"
            "* Subtle animations and transitions that enhance user experience without being distracting.\n"
            "* Icons (e.g., from Lucide Icons, Heroicons) should be used appropriately to improve visual communication.\n\n"

            "Code Generation Requirements:\n"
            "1. Guaranteed Runnable State: The generated set of files must collectively form a project that can be initialized with npm install (or yarn equivalent) and then run using npm run dev (or start) without any code modifications. The package.json must list all necessary dependencies with compatible versions.\n"
            "2. Minimum 7 essential files, but provide all necessary configuration and source files for a complete, runnable application as described in 'Project Structure & Deliverables'.\n"
            "3. Strict format for each file block:\n"
            "```<language>\n# File: <relative/path/to/file.ext>\n<code content>\n```\n"
            "4. Use mock data, placeholders, or simple functional logic as needed to make the UI interactive and demonstrate its features. Backend calls should be faked.\n"
            "5. Code must be clean, well-organized, readable, and include comments explaining key logic, component purposes, or complex configurations.\n\n"

            "Internal Pre-flight Check (AI's Self-Correction Process):\n"
            "Before finalizing the output, you must internally simulate and review the setup and execution flow. This involves:\n"
            "  a. Dependency Verification: Double-check that package.json includes all essential packages (React, ReactDOM, Vite/CRA, TypeScript, Tailwind, PostCSS, chosen UI library, routing, state management if used, etc.) and that their versions are generally compatible.\n"
            "  b. Configuration Integrity: Scrutinize vite.config.ts (or CRA equivalent), tailwind.config.js, postcss.config.js, and tsconfig.json for correct paths, plugins, and settings. Ensure Tailwind's content array correctly points to all files using Tailwind classes.\n"
            "  c. Entry Point & Imports/Exports: Verify that src/main.tsx (or index.tsx) correctly renders App.tsx, and that all component imports/exports resolve correctly. Check for common issues like incorrect file paths or default/named export mismatches.\n"
            "  d. Basic Rendering: Ensure that App.tsx and any initial page/component would render without immediate JavaScript errors (e.g., undefined variables, incorrect hook usage at a high level).\n"
            "  e. Tailwind & UI Library Initialization: Confirm that Tailwind's base styles are imported and the UI library (especially if it's Shadcn/UI) is set up in a way that its components would render with correct styling (e.g., globals.css has Tailwind directives and theme variables if needed).\n"
            "If potential issues are identified during this internal review, adjust the generated code to resolve them before outputting the final response. The goal is to achieve a high degree of confidence that the code will run 'out-of-the-box'.\n\n"

            "Goal:\n"
            "Produce a boilerplate project that not only fulfills the Jira ticket's purpose but also serves as a showcase of excellent UI/UX using the specified stack. The generated code should reflect the skill, attention to detail, and design sensibility of an experienced Senior Frontend Developer aiming for immediate runnability and visual excellence."
        )

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a highly skilled software engineer who creates production-ready codebases from requirements."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )
        return response['choices'][0]['message']['content']
