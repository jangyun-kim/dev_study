from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class SessionVectorizer:
    def __init__(self, max_features=5000):
        self.vectorizer = TfidfVectorizer(max_features=max_features)

    def fit_transform(self, texts: pd.Series):
        """
        세션별 텍스트를 TF-IDF 벡터로 변환.

        TF-IDF는 “가벼움 + 효과적”
        → SBERT보다 빠르고, Data Analyst/Engineer에게 적합.

        텍스트 전처리 없이 바로 사용해도 잘 됨.
        """
        

        X = self.vectorizer.fit_transform(texts)
        return X

        # self.vectorizer.fit_transform(texts)
        # return None
