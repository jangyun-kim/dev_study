import pandas as pd

# class 뼈대
class SessionTextAggregator:
    """
    Aggregates event-level texts into session-level documents.
    """

    def __init__(self, text_col: "event_text"):
        self.text_col = text_col

    def aggregate(self, df: pd.DataFrame) -> pd.DataFrame:
        # 핵심 매서드 정의
        """
        Input:
            df: sessionized DataFrame
                columns: [user_id, session_id, event_time, event_text]

        Output:
            DataFrame
                columns: [session_id, raw_text]
        """
        # ===============================
        # Sort events inside each session
        # text는 순서의 의미가 있으므로 event_time 기준으로 정렬 필요
        # 클렉 -> 검색 -> 결제 순서가 뒤섞이면 모델이 헷갈림.
        # ===============================
        df = df.sort_values(by=["user_id", "session_id", "event_time"])

        # ===============================
        # Session별 텍스트 결합(핵심 로직)
        # groupby(session_id)
        # 이벤트 텍스트들을 시간 순서 그대로 하나의 문장으로
        # ===============================
        session_text = (
            df.groupby(["user_id", "session_id"])[self.text_col]
            .apply(lambda x: " ".join(x))
            .reset_index()
        )
        
        # Rename aggregated text column
        session_text = session_text.rename(
            columns = {self.text_col: "raw_text"}
        )

        # ==============================
        # Create global session_id
        # ==============================
        session_text["global_session_id"] = (
            session_text["user_id"].astype(str)
            + "_"
            + session_text["session_id"].astype(str)
        )

        # ==============================
        # 텍스트 정제(cleaned_text)
        # Vectorizer / Embedding 입력은 정규화된 텍스트
        # 불필요한 특수문자 제거, 소문자화 등
        # ==============================
        session_text["cleaned_text"] = (
            session_text["raw_text"]
            .str.lower()                                    # 소문자화
            .str.replace(r"[^a-z0-0\s]", "", regex = True)  # 특수문자 제거
        )

        return session_text
    
