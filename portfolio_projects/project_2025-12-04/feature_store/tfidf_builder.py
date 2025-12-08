"""
TF-IDF Builder for session text.
"""

from sklearn.feature_extraction.text import TfidfVectorizer

class TFIDFBuilder:
    """
    세션 텍스트 데이터를 TF-IDF 벡터로 변환하는 클래스입니다.
    실무에서 가장 많이 사용되는 baseline NLP 벡터 방식입니다.
    """

    def __init__(self, max_features=5000):
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=(1, 2)
        )

    def fit_transform(self, texts):
        """
        텍스트 리스트를 입력받아 TF-IDF 행렬을 학습(fit)하고 변환(transform)까지 수행합니다.
        """
        return self.vectorizer.fit_transform(texts)

    def transform(self, texts):
        """
        이미 학습된 TF-IDF vectorizer를 이용하여 새로운 텍스트를 변환합니다.
        """
        return self.vectorizer.transform(texts)
