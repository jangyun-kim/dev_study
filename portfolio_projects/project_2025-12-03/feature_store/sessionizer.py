import pandas as pd

class Sessionizer:
    def __init__(self, inactivity_minutes=30):
        self.gap = inactivity_minutes * 60  # seconds

    def assign_sessions(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        사용자 이벤트 로그를 “세션 단위”로 나누어 session_id를 부여
        Input df columns:
            - user_id
            - event_time (datetime)
            - event_text
        Return: 세션 ID를 포함한 DataFrame
        """

        # (1) Sort: 사용자별 행동 순서를 맞춰 세션 끊김을 계산
        df = df.sort_values(by=["user_id", "event_time"])

        # (2) 이전 이벤트 시각 비교: 같은 사용자 내에서 이전 행의 시간값을 가져오는 기능.
        df["prev_time"] = df.groupby("user_id")["event_time"].shift(1)

        # (3) 시간 차이 > gap 이면 new_session
        df["time_gap"] = (df["event_time"] - df["prev_time"]).dt.total_seconds()

        ## (> self.gap) = session 분리 조건
        df["new_session"] = (df["time_gap"] > self.gap) | (df["prev_time"].isna())

        # (4) cumsum 으로 session_id 생성: new_session 값이 True일 때마다 증가
        df["session_id"] = df.groupby("user_id")["new_session"].cumsum()

        return df
