from sklearn.cluster import KMeans
import numpy as np

class IntentClusterer:
    """KMeans 기반 세션 intent clusterer"""

    def __init__(self, n_clusters=3, random_state=42):
        self.model = KMeans(n_clusters=n_clusters, random_state=random_state)

    def fit_predict(self, X: np.ndarray):
        """세션 임베딩 X에 대해 클러스터 예측"""
        return self.model.fit_predict(X)

    def get_top_keywords(self, vectorizer, n_top=5):
        """TF-IDF vocabulary에서 클러스터별 주요 단어 추출"""
        feature_names = vectorizer.get_feature_names_out()
        centers = self.model.cluster_centers_

        top_keywords = {}
        for i, center in enumerate(centers):
            idx = center.argsort()[-n_top:][::-1]
            top_keywords[i] = feature_names[idx].tolist()

        return top_keywords
