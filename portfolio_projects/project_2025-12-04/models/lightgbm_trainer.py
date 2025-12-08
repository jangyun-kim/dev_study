"""
LightGBM Trainer for Intent Classification
"""

import joblib
import lightgbm as lgb

class LightGBMTrainer:
    """
    TF-IDF + Numeric Stats 기반 Intent Multi-class Classification 모델
    """

    def __init__(self, params=None):
        default_params = {
            "objective": "multiclass",
            "num_class": 4,  # multi-class 클래스 개수
            "learning_rate": 0.05,
            "n_estimators": 200,
            "num_leaves": 32,
            "random_state": 42
        }
        self.params = params if params is not None else default_params
        self.model = lgb.LGBMClassifier(**self.params)

    def train(self, X, y):
        """
        LightGBM 모델을 학습시킵니다.
        """
        self.model.fit(X, y)
        return self.model

    def predict(self, X):
        """
        학습된 모델을 사용하여 예측합니다.
        """
        return self.model.predict(X)

    def save(self, path="models/lightgbm_model.pkl"):
        """
        모델을 디스크에 저장합니다.
        """
        joblib.dump(self.model, path)
