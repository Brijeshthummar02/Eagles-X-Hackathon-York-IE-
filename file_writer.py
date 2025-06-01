import os
import re

class FileWriter:
    def __init__(self, base_path):
        self.base_path = base_path

    def write_files(self, generated_content):
        # Match blocks like: ```<lang>\n# File: path/to/file.ext\n<code>\n```
        pattern = r"```(?:\w+)?\n# File: (.+?)\n(.*?)```"
        matches = re.findall(pattern, generated_content, re.DOTALL)

        if not matches:
            print("⚠️ No valid file blocks found in generated content.")
            return

        for filename, code in matches:
            filepath = os.path.join(self.base_path, filename.strip())
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(code.strip())
            print(f"✅ Created: {filepath}")

        print(f"📁 Project written to: {self.base_path}")
