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
v1.5.0 (2025-12-09) 
- Auto EDA system Added:
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
import shutil
from datetime import datetime


# ============================================================
# Helper: Writing text files easily
# ============================================================

def write_file(path, content):
    """Create a file and write content."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ============================================================
# Daily Project Main Generator
# ============================================================

def create_daily_project():
    """Generate a new daily project folder with templates."""

    today = datetime.now().strftime("%Y-%m-%d")
    base_path = f"portfolio_projects/project_{today}"
    print(f"Creating project folder: {base_path}")

    # Project root folders
    folders = [
        base_path,
        f"{base_path}/data",
        f"{base_path}/feature_store",
        f"{base_path}/models",
        f"{base_path}/pipelines",
        f"{base_path}/tests",
        f"{base_path}/notebooks",
        f"{base_path}/sql",
        f"{base_path}/assets",
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # ============================================================
    # 1) Python Templates
    # ============================================================

    # --- Auto EDA Template ---
    auto_eda = """\
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AutoEDA:
    \"\"\"Lightweight Auto EDA module (v1.5).\"\"\"

    def __init__(self, output_dir=\"assets\"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def run(self, df: pd.DataFrame):
        \"\"\"Generate EDA summary + visualizations.\"\"\"

        report_path = os.path.join(self.output_dir, "eda_overview.md")

        with open(report_path, "w", encoding="utf-8") as f:

            f.write("# Auto EDA Overview (v1.5)\\n\\n")

            # Data types
            f.write("## Data Types\\n")
            f.write(df.dtypes.to_markdown())
            f.write("\\n\\n")

            # Missing values
            f.write("## Missing Values\\n")
            f.write(df.isna().sum().to_markdown())
            f.write("\\n\\n")

            # Basic Stats
            f.write("## Basic Statistics\\n")
            f.write(df.describe(include='all').to_markdown())
            f.write("\\n\\n")

        # Numeric visuals
        numeric_cols = df.select_dtypes(include='number').columns

        for col in numeric_cols:
            plt.figure(figsize=(6, 3))
            sns.histplot(df[col], kde=True)
            plt.title(f"Distribution - {col}")
            plt.savefig(os.path.join(self.output_dir, f"dist_{col}.png"))
            plt.close()

        # Correlation heatmap
        if len(numeric_cols) > 1:
            plt.figure(figsize=(6, 5))
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="Blues")
            plt.title("Correlation Heatmap")
            plt.savefig(os.path.join(self.output_dir, "corr_heatmap.png"))
            plt.close()

        print(f"[AutoEDA] Report generated → {report_path}")
"""

    write_file(f"{base_path}/feature_store/auto_eda.py", auto_eda)

    # --- Feature Builder Template ---
    feature_builder = """\
import pandas as pd
from feature_store.auto_eda import AutoEDA


class FeatureBuilder:
    \"\"\"Feature Engineering Template (Daily Project).\"\"\"

    def __init__(self):
        self.eda = AutoEDA(output_dir=\"../assets\")

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        \"\"\"Return transformed dataset with engineered features.\"\"\"

        # =============================
        # Fill your code
        # =============================
        # 예: df['event_length'] = df['text'].str.len()

        # --- Auto EDA 실행 ---
        self.eda.run(df)

        return df
"""

    write_file(f"{base_path}/feature_store/feature_builder.py", feature_builder)

    # --- Pipeline Template ---
    pipeline = """\
import pandas as pd
from feature_store.feature_builder import FeatureBuilder

class PipelineRunner:

    def run(self, input_path: str, output_path: str):

        df = pd.read_csv(input_path)

        builder = FeatureBuilder()
        df_out = builder.transform(df)

        df_out.to_csv(output_path, index=False)

        print(f"[Pipeline] Completed. Saved → {output_path}")

"""

    write_file(f"{base_path}/pipelines/run_pipeline.py", pipeline)

    # ============================================================
    # SQL Template
    # ============================================================

    sql_template = """\
-- Daily SQL Template
-- Write your SQL logic here.

-- =============================
-- Fill your code
-- =============================

SELECT *
FROM raw_events;
"""

    write_file(f"{base_path}/sql/query.sql", sql_template)

    # ============================================================
    # Notebook Template
    # ============================================================

    notebook_template = """\
# Daily Project Notebook (Auto Template)
# Version: v1.5

This notebook is for exploration, visualization, and experimentation.

## Fill your analysis here.
"""

    write_file(f"{base_path}/notebooks/analysis.ipynb", notebook_template)

    # ============================================================
    # README Template
    # ============================================================

    readme = f"""\
# Daily Project — {today}

Automatically generated by `create_project.py` (v1.5).

## ✔ Today Goal
- Data ingestion
- Feature engineering
- Auto EDA
- SQL practice

## Project Structure
project_{today}/
|── data/
|── feature_store/
|── models/
|── pipelines/
|── sql/
|── tests/
|── notebooks/
|── assets/


## How to Run
cd project_{today}/pipelines
python run_pipeline.py


## What You Should Fill Manually
- feature_store/feature_builder.py → "Fill your code" 부분
- sql/query.sql
- notebooks/analysis.ipynb
"""

    write_file(f"{base_path}/README.md", readme)

    print("\n🎉 Project created successfully!\n")


# ============================================================
# Main Execution
# ============================================================

if __name__ == "__main__":
    create_daily_project()
