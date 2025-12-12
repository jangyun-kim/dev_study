import pandas as pd
import re


class FeatureEngineering:
    """
    FeatureEngineer
    - 세션 단위 텍스트를 하나로 묶고(clean),
      session_id 기준으로 aggregation을 수행.
    """

    def __init__(self):
        pass

    def aggregate_session_texts(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        session_id 기준으로 raw_text와 cleaned_text를 하나의 문장으로 묶는다.

        Args:
            df: sessionizer 결과 DataFrame (session_id 반드시 포함)
        Returns:
            fe_out: session_id, raw_text, cleaned_text 포함된 DataFrame
        """

        if "session_id" not in df.columns:
            raise ValueError("DataFrame must contain session_id column.")

        # raw_text를 합치기
        df["raw_text"] = df["event_text"]

        # cleaned_text 생성
        df["cleaned_text"] = (
            df["raw_text"]
            .str.lower()
            .str.replace(r"[^a-z0-9 ]", "", regex=True)
        )

        # session_id 기준으로 aggregation
        fe_out = (
            df.groupby("session_id")
            .agg({
                "raw_text": lambda x: " ".join(x),
                "cleaned_text": lambda x: " ".join(x),
            })
            .reset_index()
        )

        return fe_out
