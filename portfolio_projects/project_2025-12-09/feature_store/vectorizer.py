import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class TextVectorizer:
    """TextVectorizer.

    세션 단위 cleaned_text 컬럼을 입력으로 받아
    TF-IDF 기반의 embedding 행렬을 생성하는 클래스입니다.
    """

    def __init__(self, max_features: int = 300) -> None:
        """Initializer.

        Args:
            max_features: TF-IDF에서 사용할 최대 vocabulary 크기.
        """
        # TF-IDF 벡터라이저 생성
        # - max_features: 상위 N개 단어만 사용 (과적합 방지 및 차원 축소)
        # - stop_words: 의미가 약한 영어 불용어 제거
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            stop_words="english",
        )

    def fit_transform(self, df: pd.DataFrame):
        """텍스트 데이터를 TF-IDF 행렬로 변환합니다.

        Args:
            df: 'cleaned_text' 컬럼을 포함한 DataFrame.

        Returns:
            X: (n_sessions, n_features) 형태의 numpy array.
            vectorizer: 학습된 TfidfVectorizer 객체.
        """
        # 여기서 df는 함수 인자로 전달되는 지역 변수입니다.
        # 따라서 모듈 전역에 df가 있을 필요가 없습니다.
        if "cleaned_text" not in df.columns:
            raise ValueError("DataFrame must contain 'cleaned_text' column.")

        # TF-IDF 행렬 생성 (scipy sparse matrix → numpy array 변환)
        X_sparse = self.vectorizer.fit_transform(df["cleaned_text"])
        X = X_sparse.toarray()

        return X, self.vectorizer
