"""
Day3 Main Training Pipeline
"""

import pandas as pd
from feature_store.intent_feature_loader import IntentFeatureLoader
from feature_store.tfidf_builder import TFIDFBuilder
from feature_store.feature_fusion import FeatureFusion
from models.lightgbm_trainer import LightGBMTrainer


def run():
    """
    Day3 전체 파이프라인 실행:
    1) Load session features
    2) TF-IDF vectorize
    3) numeric stats 결합
    4) LightGBM 모델 학습
    """
    print("[INFO] Loading session features...")
    loader = IntentFeatureLoader()
    df = loader.load()

    print("[INFO] TF-IDF vectorizing...")
    tfidf_builder = TFIDFBuilder()
    tfidf_matrix = tfidf_builder.fit_transform(df["session_text"])

    numeric_cols = ["event_count", "unique_event_count", "mean_gap", "max_gap"]
    stats_df = df[numeric_cols]

    print("[INFO] Combining sparse text features + numeric stats...")
    fusion = FeatureFusion()
    X = fusion.combine(tfidf_matrix, stats_df)

    print("[INFO] Training LightGBM model...")
    trainer = LightGBMTrainer()
    model = trainer.train(X, df["intent_label"])
    trainer.save()

    print("[INFO] Training completed. Model saved to models/lightgbm_model.pkl")


if __name__ == "__main__":
    run()
