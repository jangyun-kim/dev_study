# models/baseline.py
from sklearn.linear_model import LogisticRegression
from sklearn.metricts import roc_auc_score, log_loss

class BaselineCTRModel:
    """기본 Logistic Regression 기반 CTR 예측 모델 템플릿"""

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
