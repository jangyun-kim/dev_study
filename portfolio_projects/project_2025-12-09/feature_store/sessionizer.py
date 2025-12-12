import pandas as pd

class Sessionizer:
    """
    Sessionizer class
    - 사용자 이벤트 로그를 inactivity window 기준으로 session 단위로 분리
    """

    def __init__(self, inactivity_minutes=30):
        self.gap = inactivity_minutes * 60  # seconds

    def assign_sessions(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        사용자 이벤트 로그 df에 session_id 를 부여합니다.
        df columns:
            - user_id (int)
            - event_time (datetime)
            - event_text (str)
        """
        df = df.sort_values(by=["user_id", "event_time"]).copy()
        df["prev_time"] = df.groupby("user_id")["event_time"].shift(1)
        df["time_gap"] = (df["event_time"] - df["prev_time"]).dt.total_seconds()

        # 새로운 세션 조건
        df["new_session"] = (df["time_gap"] > self.gap) | (df["prev_time"].isna())

        # session_id 생성
        df["session_id"] = df.groupby("user_id")["new_session"].cumsum()

        return df
