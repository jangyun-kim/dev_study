from sklearn.cluster import KMeans

class SessionClusterer:
    """
    Clusters session vectors into intent groups.
    """

    # ==============================
    # Clusterer 클래스 설계
    # n_cluster: 비즈니스에서 조절 가능
    # random_state: 재현성
    # n_init = 10: 안정적인 수렴
    #===============================
    def __init__(self, n_clusters = 3, random_state = 42):
        self.model = KMeans(
            n_clusters = n_clusters,
            random_state = random_state,
            n_init = 10,
        )

    # ==============================
    # fit_predict 메서드
    # ==============================
    def fit_predict(self, X):
        """
        Input:
            X: TF-IDF matrix

        Output:
            labels: cluster assignment per session
        """
        labels = self.model.fit_predict(X)
        return labels
    
    