"""
====================================================================
create_project.py
Template Version: v1.8.0

Project structure manager for long-running data pipeline projects.
This script ensures that required directories and template files exist,
without overwriting existing implementations.

This tool is intended to be run:
- when a new pipeline stage is added
- when a new language (SQL / Java) is introduced
- when template synchronization is needed
====================================================================

Version Management Policy (Semantic Versioning)
------------------------------------------------
- MAJOR: Breaking changes (폴더 구조, 템플릿 구조 대규모 변경)
- MINOR: 새로운 기능 추가 (Notebook, SQL 샘플 등)
- PATCH: 버그 수정, 경로 문제 해결, 작은 개선

CHANGE LOG
------------------------------------------------
v1.8.0 (2025-12-17):
- Switched role from "project generator" to "structure manager"
- Safe creation: does NOT overwrite existing files
- Supports Python / SQL / Java multi-language pipeline

v1.7.0 (2025-12-09):
- Added dynamic file generation system with '--gen' argument
- AI-aware mode: Project can generate only the files needed for today's task
- Imports templates from ./templates/feature_store, model, pipelines, tests, sql
- Notebook JSON generation kept from v1.6.0
- Auto EDA notebook included
- Versioning & changelog block added
- README template upgraded

v1.6.0 (2025-12-09)
- Added FULL Jupyter Notebook JSON generator
- Added auto_eda.ipynb creation (Auto EDA workflow)
- Added feature_analysis.ipynb & model_experiment.ipynb
- Improved README template with business scenario section
- Added semantic versioning system & changelog block
- Enhanced folder creation & template handling

v1.5.0 (2025-12-09)
- Auto EDA system Added
- Lightweight Auto EDA module added (missing, stats, plot, heatmap)

v1.4.0 (2025-12-09)
- Added internal CHANGE_LOG section for version tracking
- Improved template version injection into daily README
- Prepared system for automatic version synchronization in README

v1.3.0 (2025-12-09)
- Unified version system: Daily project versions removed
- Global Template Version only
- Daily README cleanup + footer version auto insert

v1.2.0 (2025-12-08)
- Added Notebook Template
- Added Feature Engineering sample code
- Added SQL sample analysis template

v1.1.0 (2025-12-08)
- Added full template system (python/sql/markdown/tests)
- Placeholder replacement logic

v1.0.0 (2025-12-07)
- Initial pipeline generator implemented

"""

import os

# ===== Configuration =====
PROJECT_ROOT = "portfolio_projects/session_intent_pipeline"

REQUIRED_STRUCTURE = {
    "data/raw": [],
    "data/processed": [],
    "feature_store": [
        "__init__.py",
        "sessionizer.py",
        "aggregator.py",
    ],
    "pipelines": [
        "__init__.py",
        "run_pipeline.py",
    ],
    "sql": [
        "session_validation.sql",
        "session_stats.sql",
    ],
    "java": [
        "SessionJob.java",
    ],
    "notebooks": [
        "analysis.ipynb",
    ],
    "tests": [
        "test_sessionizer.py",
    ],
}

FILL_MARK = """# ====================
#        Fill your code
# ====================
"""


def safe_create_dir(path: str) -> None:
    """Create directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"[CREATE DIR] {path}")


def safe_create_file(path: str, filename: str) -> None:
    """Create file with Fill-your-code marker if it does not exist."""
    full_path = os.path.join(path, filename)
    if not os.path.exists(full_path):
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(FILL_MARK)
        print(f"[CREATE FILE] {full_path}")


def main() -> None:
    print("[INFO] Project structure check started")

    for folder, files in REQUIRED_STRUCTURE.items():
        dir_path = os.path.join(PROJECT_ROOT, folder)
        safe_create_dir(dir_path)

        for file in files:
            safe_create_file(dir_path, file)

    print("[OK] Project structure is up to date")


if __name__ == "__main__":
    main()