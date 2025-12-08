"""
====================================================================
create_project.py
Daily Portfolio Project Generator
Template Version: v1.5
====================================================================

Version Management Policy (Semantic Versioning)
------------------------------------------------
- MAJOR: Breaking changes (폴더 구조, 템플릿 구조 대규모 변경)
- MINOR: 새로운 기능 추가 (Notebook, SQL 샘플 등)
- PATCH: 버그 수정, 경로 문제 해결, 작은 개선

CHANGE LOG
------------------------------------------------
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

v1.3 (2025-12-09)
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
import json
import argparse
from datetime import datetime
import shutil


# ============================================================
# Utility: Load a template file from templates/
# ============================================================

def load_template(rel_path: str) -> str:
    """
    템플릿 파일을 ./templates/ 경로에서 불러오는 함수.
    존재하지 않을 경우 빈 문자열 반환.
    """
    full_path = os.path.join("templates", rel_path)

    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return f"# Template not found for {rel_path}\n\n# ====================\n#   Fill your code\n# ====================\n"


# ============================================================
# Notebook JSON generator
# ============================================================

def generate_notebook_json(title: str, intro_text: str):
    """올바른 JSON 포맷의 Jupyter Notebook 생성"""
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n\n",
                    intro_text,
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Notebook initialized\n",
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "print('Notebook Ready!')"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }


def generate_auto_eda_notebook():
    """Auto EDA 전용 Notebook"""
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Auto EDA Notebook\n",
                    "자동 분석(EDA)을 위한 기본 코드가 포함되어 있습니다.\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import pandas as pd\n",
                    "import seaborn as sns\n",
                    "import matplotlib.pyplot as plt\n\n",
                    "df = pd.read_csv('../data/raw/raw_events.csv')\n",
                    "df.head()"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }


# ============================================================
# README Generator
# ============================================================

def generate_readme(project_date):
    return f"""
# Daily Project — {project_date}

이 프로젝트는 매일의 실전 분석 역량 강화를 위해 자동 생성됩니다.

---

## 프로젝트 목적
- 세션 기반 로그 분석과 ML Feature Engineering 경험 축적
- 실무형 파이프라인 설계 능력 강화
- 매일 하나씩 포트폴리오 성장

---

## 주요 자동 생성 요소
- /data/raw
- /data/processed
- /feature_store
- /model
- /sql
- /tests
- /notebooks

---

## Run
python pipelines/run_pipeline.py

## Test
qytest -q


---

## 📘 Version
v0.1.0 — {project_date}
"""


# ============================================================
# Generate project
# ============================================================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--gen",
        type=str,
        default="all",
        help="Generate specific modules: feature, model, pipeline, tests, sql, notebooks, all"
    )
    args = parser.parse_args()

    today = datetime.now().strftime("%Y-%m-%d")
    base = os.path.join("portfolio_projects", f"project_{today}")
    os.makedirs(base, exist_ok=True)

    # 기본 디렉토리 생성
    dirs = [
        "data/raw",
        "data/processed",
        "feature_store",
        "model",
        "notebooks",
        "sql",
        "tests",
        "pipelines"
    ]

    for d in dirs:
        os.makedirs(os.path.join(base, d), exist_ok=True)

    # ---------------------------------------------
    # ALWAYS generate notebooks + README
    # ---------------------------------------------
    notebooks = {
        "analysis.ipynb": generate_notebook_json(
            "Daily Analysis Notebook", "오늘 분석 내용을 이곳에 작성하세요."
        ),
        "feature_analysis.ipynb": generate_notebook_json(
            "Feature Engineering Notebook", "Feature engineering 과정을 기록합니다."
        ),
        "model_experiment.ipynb": generate_notebook_json(
            "Model Experiment Notebook", "모델 실험과 튜닝 결과를 기록합니다."
        ),
        "auto_eda.ipynb": generate_auto_eda_notebook()
    }

    for name, nb in notebooks.items():
        save_path = os.path.join(base, "notebooks", name)
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, ensure_ascii=False, indent=2)

    # README 생성
    with open(os.path.join(base, "README.md"), "w", encoding="utf-8") as f:
        f.write(generate_readme(today))

    # ---------------------------------------------
    # Dynamic file generation
    # ---------------------------------------------

    selected = args.gen.split(",")  # 예: ["feature","tests"]

    def generate_if_needed(keyword, rel_template_path, dest_file_path):
        """선택된 경우에만 템플릿 파일을 복사하여 생성"""
        if "all" in selected or keyword in selected:
            content = load_template(rel_template_path)
            with open(os.path.join(base, dest_file_path), "w", encoding="utf-8") as f:
                f.write(content)

    # feature_store templates
    generate_if_needed("feature", "feature_store/sessionizer.py", "feature_store/sessionizer.py")
    generate_if_needed("feature", "feature_store/feat_eng.py", "feature_store/feat_eng.py")
    generate_if_needed("feature", "feature_store/vectorizer.py", "feature_store/vectorizer.py")
    generate_if_needed("feature", "feature_store/model_input_builder.py", "feature_store/model_input_builder.py")

    # model templates
    generate_if_needed("model", "model/intent_model.py", "model/intent_model.py")

    # pipelines
    generate_if_needed("pipeline", "pipelines/run_pipeline.py", "pipelines/run_pipeline.py")

    # tests
    generate_if_needed("tests", "tests/test_feature_store.py", "tests/test_feature_store.py")
    generate_if_needed("tests", "tests/test_model_pipeline.py", "tests/test_model_pipeline.py")

    # sql
    generate_if_needed("sql", "sql/01_basic_analysis.sql", "sql/01_basic_analysis.sql")
    generate_if_needed("sql", "sql/02_session_stats.sql", "sql/02_session_stats.sql")

    print(f"[SUCCESS] Project created → {base}")
    print(f"[INFO] created Module: {selected}")


if __name__ == "__main__":
    main()


