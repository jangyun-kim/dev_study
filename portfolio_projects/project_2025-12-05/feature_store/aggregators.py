# feature_store/aggregators.py
import pandas as pd

class FeatureAggregator:
    """피처 집계 클래스 (Day 0 버전)"""

    def aggregate_user_features(self, df):
        """유저별 이벤트 카운트 기본 집계"""

        # ======================================
        #             Fill your code
        # ======================================
        feat = (
            df.groupby('user_id')
              .agg(event_count=('event_type', 'count'))
              .reset_index()
        )
        return feat
