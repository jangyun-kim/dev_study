# feature_store/loader.py
import pandas as pd

class FeatureLoader:
    """원천 로그 로더 클래스"""

    def load_logs(self, path: str):
        """CSV 파일을 로드하고 기본적인 컬럼 검증을 수행합니다."""

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
