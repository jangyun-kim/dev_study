"""
create_project.py
Version: v1.0.0 (2025-12-08)

Semantic Versioning (SemVer):
- MAJOR: Breaking changes (기존 구조와 비호환)
- MINOR: New features added (기존 기능과 호환)
- PATCH: Bug fixes / small improvements

Change Log:
- v0.5.0:
    * 프로젝트 생성 기능 완전 재설계
    * Day별 project_type(de_pipeline, ml_retrieval, experiment 등) 지원
    * templates 폴더를 실제로 활용하도록 구조 변경
    * notebooks/, assets/plots, assets/diagrams 자동 생성 추가
    * Fill your code 영역 자동 삽입 기능 추가
- v0.4.1:
    * 템플릿 구조 일부 도입
    * 불필요 폴더 제거
- v0.4.0:
    * 최초 Daily Project Generator 추가
- v1.0.0:
    * Template 기반 프로젝트 생성 시스템 완성

주요 기능:
 - templates/ 폴더 내부의 템플릿 파일 자동 로드
 - placeholder 자동 치환 ({{DATE}}, {{PROJECT_NAME}} 등)
 - 매일 project_YYYY-MM-DD 폴더 생성
 - 정해진 구조(pipelines, builder, evaluator, sql, notebooks, tests) 자동 생성
 - README, instructions, concepts 문서 자동 생성

버전 규칙:
  Major.Minor.Patch
  1.0.0 → 템플릿 시스템 전체 완성
"""

import os
import shutil
from datetime import datetime


# -----------------------------------------------------------
# Helper: 템플릿 파일 내용을 placeholder 치환하여 읽기
# -----------------------------------------------------------
def load_and_format_template(template_path: str, replacements: dict) -> str:
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    for key, value in replacements.items():
        content = content.replace(f"{{{{{key}}}}}", value)

    return content


# -----------------------------------------------------------
# Daily Project Generator
# -----------------------------------------------------------
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

    # --------------------------------------------------------
    # Python 템플릿 복사
    # --------------------------------------------------------
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
            src_path = os.path.join(src, src_file)
            dst_path = os.path.join(self.project_dir, dst_file)

            shutil.copy(src_path, dst_path)

    # --------------------------------------------------------
    # SQL 템플릿 복사
    # --------------------------------------------------------
    def copy_sql_templates(self):
        src = os.path.join(self.templates_dir, "sql")
        dst = os.path.join(self.project_dir, "sql")

        for file in os.listdir(src):
            shutil.copy(os.path.join(src, file), dst)

    # --------------------------------------------------------
    # Notebook 템플릿 복사
    # --------------------------------------------------------
    def copy_notebook_template(self):
        src = os.path.join(self.templates_dir, "notebooks")
        dst = os.path.join(self.project_dir, "notebooks")

        for file in os.listdir(src):
            shutil.copy(os.path.join(src, file), dst)

    # --------------------------------------------------------
    # Markdown 템플릿 복사 + 치환
    # --------------------------------------------------------
    def copy_markdown_templates(self):
        md_src = os.path.join(self.templates_dir, "markdown")

        replacements = {
            "DATE": self.date,
            "PROJECT_NAME": f"Daily Project {self.date}"
        }

        md_files = {
            "readme_template.md": "README.md",
            "instructions_template.md": "instructions.md",
            "concepts_template.md": "concepts.md"
        }

        for src_file, dst_file in md_files.items():
            src_path = os.path.join(md_src, src_file)
            dst_path = os.path.join(self.project_dir, dst_file)

            output = load_and_format_template(src_path, replacements)

            with open(dst_path, "w", encoding="utf-8") as f:
                f.write(output)

    # --------------------------------------------------------
    # Execute
    # --------------------------------------------------------
    def generate(self):
        print(f"\n🚀 Creating new project for {self.date}...\n")

        self.create_base_structure()
        self.copy_python_templates()
        self.copy_sql_templates()
        self.copy_notebook_template()
        self.copy_markdown_templates()

        print(f"✨ Project created: {self.project_dir}")
        print("👉 README, instructions, concepts generated.")
        print("👉 Fill your code sections are ready.\n")


# --------------------------------------------------------
# Script Entry
# --------------------------------------------------------
if __name__ == "__main__":
    generator = ProjectGenerator()
    generator.generate()
