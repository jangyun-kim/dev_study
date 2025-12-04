#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily Project Scaffolding Tool
--------------------------------
매일 프로젝트 스캐폴딩을 자동 생성하는 스크립트입니다.
폴더 구조, 템플릿 파일, 테스트 파일, README까지 자동 생성됩니다.

실행:
    python create_project.py
"""

import os
import datetime
from pathlib import Path
base_dir = Path.home() / "Google Drive" / "dev_portfolio" / "portfolio_projects"



# BASE_DIR = "./portfolio_projects"


# =========================================
# Template Files
# =========================================

FEATURE_TEMPLATE = """# feature_store/loader.py
import pandas as pd

class FeatureLoader:
    \"\"\"원천 로그 로더 클래스\"\"\"

    def load_logs(self, path: str):
        \"\"\"CSV 파일을 로드하고 기본적인 컬럼 검증을 수행합니다.\"\"\"

        # ======================================
        #             Fill your code
        # ======================================
        try:
            df = pd.read_csv(path)
        except Exception as e:
            raise ValueError(f"Failed to load {path}: {e}")

        required_cols = {'user_id', 'item_id', 'event_type', 'ts'}
        if not required_cols.issubset(df.columns):
            raise ValueError(f"Required columns missing: {required_cols}")

        return df
"""


AGG_TEMPLATE = """# feature_store/aggregators.py
import pandas as pd

class FeatureAggregator:
    \"\"\"피처 집계 클래스 (Day 0 버전)\"\"\"

    def aggregate_user_features(self, df):
        \"\"\"유저별 이벤트 카운트 기본 집계\"\"\"

        # ======================================
        #             Fill your code
        # ======================================
        feat = (
            df.groupby('user_id')
              .agg(event_count=('event_type', 'count'))
              .reset_index()
        )
        return feat
"""


MODEL_TEMPLATE = """# models/baseline.py
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, log_loss

class BaselineCTRModel:
    \"\"\"기본 Logistic Regression 기반 CTR 예측 모델 템플릿\"\"\"

    def __init__(self):
        self.model = LogisticRegression(max_iter=200)

    def fit(self, X, y):

        # ======================================
        #             Fill your code
        # ======================================
        return self.model.fit(X, y)

    def evaluate(self, X, y):

        # ======================================
        #             Fill your code
        # ======================================
        pred = self.model.predict_proba(X)[:, 1]
        return {
            "AUC": roc_auc_score(y, pred),
            "LogLoss": log_loss(y, pred)
        }
"""


RUN_TEMPLATE = """# run_pipeline.py
\"\"\"Day 0 데모 파이프라인 실행 스크립트\"\"\"
import logging
from feature_store.loader import FeatureLoader
from feature_store.aggregators import FeatureAggregator

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Pipeline started.")

    loader = FeatureLoader()
    agg = FeatureAggregator()

    try:
        # 아래 경로 변경 가능

        # ======================================
        #             Fill your code
        # ======================================
        df = loader.load_logs("data/sample_log.csv")

        # ======================================
        #             Fill your code
        # ======================================
        features = agg.aggregate_user_features(df)

        logging.info(f"Generated features:\\n{features.head()}")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

    logging.info("Pipeline completed.")
"""


TEST_TEMPLATE = """# tests/test_feature_store.py
import unittest
import pandas as pd
from feature_store.loader import FeatureLoader

class TestFeatureStore(unittest.TestCase):

    def test_loader(self):
        # 샘플 CSV 생성

        # ======================================
        #             Fill your code
        # ======================================
        sample = pd.DataFrame({
            'user_id': [1, 2],
            'item_id': [10, 20],
            'event_type': ['view', 'click'],
            'ts': ['2025-01-01 10:00', '2025-01-01 10:02']
        })
        sample.to_csv('tests/sample.csv', index=False)

        loader = FeatureLoader()
        loaded = loader.load_logs('tests/sample.csv')

        assert len(loaded) == 2


if __name__ == '__main__':
    unittest.main()
"""


README_TEMPLATE = """# Daily Project

**Date:** {today}

## 📌 Day 0 — Demo Project

### 1. Business Case
간단한 사용자 로그에서 유저별 이벤트 수 집계를 생성하는 데모 프로젝트입니다.

### 2. Folder Structure
feature_store/
models/
tests/
run_pipeline.py
README.md


### 3. How to Run
python run_pipeline.py


### 4. Testing
pytest tests/

"""


# =========================================
# Project Creator Function
# =========================================

def create_project_folder():
    today = datetime.date.today().strftime("%Y-%m-%d")
    project_name = f"project_{today}"
    project_dir = os.path.join(BASE_DIR, project_name)

    os.makedirs(project_dir, exist_ok=True)
    os.makedirs(f"{project_dir}/feature_store", exist_ok=True)
    os.makedirs(f"{project_dir}/models", exist_ok=True)
    os.makedirs(f"{project_dir}/tests", exist_ok=True)
    os.makedirs(f"{project_dir}/data", exist_ok=True)

    file_map = {
        f"{project_dir}/feature_store/loader.py": FEATURE_TEMPLATE,
        f"{project_dir}/feature_store/aggregators.py": AGG_TEMPLATE,
        f"{project_dir}/models/baseline.py": MODEL_TEMPLATE,
        f"{project_dir}/run_pipeline.py": RUN_TEMPLATE,
        f"{project_dir}/tests/test_feature_store.py": TEST_TEMPLATE,
        f"{project_dir}/README.md": README_TEMPLATE.format(today=today),
    }

    for path, content in file_map.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"[SUCCESS] Project folder created:\n  {project_dir}")


# =========================================
# Main
# =========================================

if __name__ == "__main__":
    create_project_folder()
