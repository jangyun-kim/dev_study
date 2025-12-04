from sklearn.cluster import KMeans

class IntentClusterer:
    def __init__(self, k=8):
        self.k = k
        self.model = KMeans(n_clusters=k, random_state=42)

    def fit_predict(self, X):
        """
        TF-IDF 출력을 기반으로 의도(intent) 클러스터를 생성.
        KMeans는:
            - session intent segmentation의 기본 중 기본
            - 빠르고 해석 용이
            - 군집 중심(cluster center)을 바탕으로 유저 행동 의도 패턴 해석 가능

        실무 활용:
            - 검색어 분류
            - 행동 기반 타겟팅 유저 그룹 생성
            - 쇼핑 행동 / 스크롤 패턴 분석
            - 차량 이벤트 패턴 클러스터링
        """

        labels = self.model.fit_predict(X)
        return labels

        return None
