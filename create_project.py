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
from datetime import datetime

# -----------------------------------------------------
# Notebook Template JSON
# -----------------------------------------------------

def generate_notebook_json(title: str, intro_text: str):
    """Return valid Jupyter Notebook JSON"""

    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# 📘 {title}\n\n",
                    intro_text,
                    "\n\n---\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 기본 실행 코드 셀\n",
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "print('Notebook initialized!')"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

# -----------------------------------------------------
# Auto EDA Notebook Template
# -----------------------------------------------------

def generate_auto_eda_notebook():
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# 🔍 Auto EDA Notebook\n\n",
                    "자동 EDA 수행을 위한 기본 코드가 포함.\n",
                    "Raw 데이터 구조 파악 → 결측치 분석 → 통계 분석 → 시각화까지 자동화.\n"
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
                    "import matplotlib.pyplot as plt\n",
                    "\n",
                    "# 데이터 로딩\n",
                    "df = pd.read_csv('../data/raw/raw_events.csv')\n",
                    "df.head()"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 데이터 기본 정보\n",
                    "df.info()"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 결측치 분석\n",
                    "df.isnull().sum()"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 기본 통계\n",
                    "df.describe(include='all')"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 주요 수치형 컬럼 histogram\n",
                    "numeric_cols = df.select_dtypes(include=['int', 'float']).columns\n",
                    "df[numeric_cols].hist(figsize=(10, 6))\n",
                    "plt.show()"
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

# -----------------------------------------------------
# README Template
# -----------------------------------------------------

def generate_readme(project_date):
    return f"""
# 📌 Daily Project — {project_date}

이 프로젝트는 매일 하나의 실무형 분석·엔지니어링 과제를 수행하며 포트폴리오를 구축하기 위한 자동 생성 템플릿.

---

## 🎯 프로젝트 목적  
- 실제 기업 환경에서 사용하는 Session 기반 분석, NLP 기반 Feature Engineering, ML 파이프라인 등을 구현  
- 코드 구조화, 테스트 자동화, SQL 분석 역량 강화  
- 매일 하나의 완성된 분석 결과를 남겨 포트폴리오 자산으로 활용  

---

## 📂 생성된 폴더 구조

- `data/raw/`        → 원천 로그 데이터  
- `data/processed/`  → 세션/특징 가공 데이터  
- `feature_store/`   → Sessionizer, Feature Engineering, Vectorizer  
- `model/`           → 모델 학습 파일  
- `notebooks/`       → Auto EDA, Feature Analysis, Model Experiment  
- `sql/`             → SQL 분석 예시  
- `tests/`           → pytest 기반 자동 테스트  

---

## 🚀 시작 방법
python pipelines/run_pipeline.py


---

## 📘 Version History

### v0.1.0 ({project_date})
- 프로젝트 초기 생성  
- Notebook/SQL/Test 구조 자동 생성  

"""

# -----------------------------------------------------
# MAIN FUNCTION — PROJECT CREATION
# -----------------------------------------------------

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    base_path = os.path.join("portfolio_projects", f"project_{today}")

    os.makedirs(base_path, exist_ok=True)

    # Create directories
    subfolders = [
        "data/raw", "data/processed",
        "feature_store", "model",
        "notebooks", "sql", "tests"
    ]

    for folder in subfolders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    # -------------------------------------------------
    # Create Notebook Files
    # -------------------------------------------------

    notebooks = {
        "analysis.ipynb": generate_notebook_json(
            "Daily Project Analysis",
            "오늘 프로젝트의 분석 기록을 이곳에 작성."
        ),
        "feature_analysis.ipynb": generate_notebook_json(
            "Feature Engineering Analysis",
            "Feature Engineering 실험을 기록하는 노트북."
        ),
        "model_experiment.ipynb": generate_notebook_json(
            "Model Experiment Notebook",
            "모델 학습 및 파라미터 튜닝 내용을 기록."
        ),
        "auto_eda.ipynb": generate_auto_eda_notebook()
    }

    for filename, json_data in notebooks.items():
        with open(os.path.join(base_path, "notebooks", filename), "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

    # -------------------------------------------------
    # Create README.md
    # -------------------------------------------------

    with open(os.path.join(base_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(generate_readme(today))

    print(f"[SUCCESS] Project created: {base_path}")

# -----------------------------------------------------

if __name__ == "__main__":
    main()

