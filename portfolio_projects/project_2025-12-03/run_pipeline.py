# run_pipeline.py
"""Day 0 데모 파이프라인 실행 스크립트"""
import logging
from feature_store.loader import FeatureLoader
from feature_store.aggregators import FeatureAggregator

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Pipeline started.")

    loader = FeatureLoader()
    agg = FeatureAggregator()

    try:
        # 아래 경로 변경 가능

        # ======================================
        #             Fill your code
        # ======================================
        df = loader.load_logs("data/sample_log.csv")

        # ======================================
        #             Fill your code
        # ======================================
        features = agg.aggregate_user_features(df)

        logging.info(f"Generated features:\n{features.head()}")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

    logging.info("Pipeline completed.")
