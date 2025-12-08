"""
Feature Fusion: TF-IDF sparse matrix + numeric statistical features 결합
"""

import numpy as np
from scipy.sparse import hstack

class FeatureFusion:
    """
    벡터화된 텍스트 + numeric features (통계치)를 하나의 feature matrix로 결합하는 클래스입니다.
    """

    def combine(self, tfidf_matrix, numeric_df):
        numeric_array = numeric_df.values  # shape: (N, K)

        # ============================
        #         Fill your code
        #  (추가 numeric 전처리, scaling 등을 포함할 수 있음)
        # ============================

        return hstack([tfidf_matrix, numeric_array])
