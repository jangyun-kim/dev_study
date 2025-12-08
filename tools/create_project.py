"""
====================================================================
create_project.py — Daily Project Generator (Template System v1.4)
====================================================================

Version Management Policy (Semantic Versioning)
------------------------------------------------
- MAJOR: Breaking changes (폴더 구조, 템플릿 구조 대규모 변경)
- MINOR: 새로운 기능 추가 (Notebook, SQL 샘플 등)
- PATCH: 버그 수정, 경로 문제 해결, 작은 개선

CHANGE LOG
------------------------------------------------
v1.4 (2025-12-09)
- Added internal CHANGE_LOG section for version tracking
- Improved template version injection into daily README
- Prepared system for automatic version synchronization in README

v1.3 (2025-12-09)
- Unified version system: Daily project versions removed
- Global Template Version only
- Daily README cleanup + footer version auto insert

v1.2 (2025-12-09)
- Added Notebook Template
- Added Feature Engineering sample code
- Added SQL sample analysis template

v1.1 (2025-12-08)
- Added full template system (python/sql/markdown/tests)
- Placeholder replacement logic

v1.0 (2025-12-07)
- Initial pipeline generator implemented
"""

import os
import shutil
from datetime import datetime

# ============================================================
# 🔥 Global Template Version — only this version is maintained
# ============================================================
TEMPLATE_VERSION = "v1.4"


def load_and_format_template(template_path: str, replacements: dict) -> str:
    """템플릿 파일을 불러와 placeholder를 치환."""
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    for key, value in replacements.items():
        content = content.replace(f"{{{{{key}}}}}", value)

    return content


class ProjectGenerator:

    def __init__(self):
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.templates_dir = os.path.join(self.root_dir, "templates")
        self.projects_dir = os.path.join(self.root_dir, "portfolio_projects")

        today = datetime.now().strftime("%Y-%m-%d")
        self.date = today
        self.project_dir = os.path.join(self.projects_dir, f"project_{today}")

    def create_base_structure(self):
        folders = [
            "pipelines",
            "builder",
            "evaluator",
            "sql",
            "notebooks",
            "tests",
            "assets",
        ]
        os.makedirs(self.project_dir, exist_ok=True)

        for folder in folders:
            os.makedirs(os.path.join(self.project_dir, folder), exist_ok=True)

    def copy_python_templates(self):
        src = os.path.join(self.templates_dir, "python")
        dst_map = {
            "pipeline_template.py": "pipelines/run_pipeline.py",
            "builder_template.py": "builder/dataset_builder.py",
            "evaluator_template.py": "evaluator/model_evaluator.py",
            "test_template.py": "tests/test_project.py",
            "logger_template.py": "pipelines/logger_config.py"
        }

        for src_file, dst_file in dst_map.items():
            shutil.copy(os.path.join(src, src_file), os.path.join(self.project_dir, dst_file))

    def copy_sql_templates(self):
        src = os.path.join(self.templates_dir, "sql")
        dst = os.path.join(self.project_dir, "sql")
        for file in os.listdir(src):
            shutil.copy(os.path.join(src, file), dst)

    def copy_notebook_template(self):
        src = os.path.join(self.templates_dir, "notebooks")
        dst = os.path.join(self.project_dir, "notebooks")
        for file in os.listdir(src):
            shutil.copy(os.path.join(src, file), dst)

    def copy_markdown_templates(self):
        md_src = os.path.join(self.templates_dir, "markdown")

        replacements = {
            "DATE": self.date,
            "PROJECT_NAME": f"Daily Project {self.date}",
            "TEMPLATE_VERSION": TEMPLATE_VERSION
        }

        md_files = {
            "readme_template.md": "README.md",
            "instructions_template.md": "instructions.md",
            "concepts_template.md": "concepts.md"
        }

        for src_file, dst_file in md_files.items():
            src_path = os.path.join(md_src, src_file)
            dst_path = os.path.join(self.project_dir, dst_file)

            content = load_and_format_template(src_path, replacements)

            # 🔥 Daily Version 제거
            content = content.replace("## Version", "")
            content = content.replace("{{VERSION}}", "")

            # 🔥 Global Template Version Footer
            content += f"\n---\n**Template Version: {TEMPLATE_VERSION}**\n"

            with open(dst_path, "w", encoding="utf-8") as f:
                f.write(content)

    def generate(self):
        print(f"\n🚀 Creating new project for {self.date}...\n")

        self.create_base_structure()
        self.copy_python_templates()
        self.copy_sql_templates()
        self.copy_notebook_template()
        self.copy_markdown_templates()

        print(f"✨ Project created: {self.project_dir}")
        print("👉 Template Version applied:", TEMPLATE_VERSION)
        print("👉 Version History embedded inside create_project.py CHANGE LOG section.")


if __name__ == "__main__":
    generator = ProjectGenerator()
    generator.generate()
