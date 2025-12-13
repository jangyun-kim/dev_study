# featrue_stroe/vectorizer.py

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class SessionVectorizer:
    """
    Converts session-level texts into numerical vectors.
    """

    def __init__(
        self,
        max_features = 1000,
        ngram_range = (1, 2),
        min_df = 1,
    ):
        self.vectorizer = TfidfVectorizer(
            max_features = max_features,
            ngram_range = ngram_range,
            min_df = min_df,
        )
    
    # =========================
    # 핵심 메서드: fit_transform
    # =========================
    def fit_transform(self, df: pd.DataFrame):
        """
        Input:
            df columns:
                - global_session_id
                - cleaned_text

        Output:
            X: TF-IDF matrix
            vectorizer: fitted vectorizer
        """

        # ========================
        # 벡터화 로직
        #   - DataFrame 전체를 넣지 않아야 한다.
        #   - 항상 text list만
        # ========================
        texts = df["cleaned_text"].tolist()

        X = self.vectorizer.fit_transform(texts)

        return X, self.vectorizer

