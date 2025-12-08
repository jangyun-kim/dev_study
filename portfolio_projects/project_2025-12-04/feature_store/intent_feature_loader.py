"""
Intent Feature Loader: Day3에서 사용할 session_intents.csv 불러오기
"""

import pandas as pd

class IntentFeatureLoader:
    """
    session_intents.csv를 읽고 모델 학습에 필요한 column을 반환하는 Loader입니다.
    """

    def __init__(self, path="data/session_intents.csv"):
        self.path = path

    def load(self):
        df = pd.read_csv(self.path)

        # session_text 컬럼이 반드시 존재해야 함
        if "session_text" not in df.columns:
            raise ValueError("session_intents.csv must contain 'session_text'")

        return df
