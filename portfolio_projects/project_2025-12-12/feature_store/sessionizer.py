# feature_store/sessionizer.py
import pandas as pd

class Sessionizer:
    def __init__(self, inactivity_minutes=30):
        self.gap = inactivity_minutes * 60

    def assign_sessions(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        사용자 이벤트 로그를 세션 단위로 나누어 session_id 부여

        Parameters
        ----------
        df : pd.DataFrame
            user_id, event_time, event_text 컬럼을 포함한 DataFrame

        Returns
        -------
        pd.DataFrame
            session_id 컬럼이 추가된 DataFrame
        """

        # ====================
        #   Fill your code
        # 1) sort_values
        # 2) groupby + shift
        # 3) time_gap 계산
        # 4) cumsum으로 session_id 생성
        # ====================

        # user_id + event_time 기준 정렬
        df = df.sort_values(['user_id', 'event_time'])

        # 같은 사용자 내에서 이전 이벤트 시간 가져오기
        df['prev_time'] = df.groupby('user_id')['event_time'].shift(1)

        # 이전 이벤트와의 시간 차이 계산(초)
        df['time_gap'] = (
            df['event_time'] - df['prev_time']
        ).dt.total_seconds()

        # 새 세션 조건
        # - 이전 이벤트가 없거나
        # - inactivity gap 초과 시
        df["new_session"] = (
            (df["prev_time"].isna()) |
            (df["time_gap"] > self.gap)
        )

        # new_session이 True일 때마다 session_id 증가
        df['session_id'] = (
            df.groupby("user_id")["new_session"]\
            .cumsum()
        )
        
        return df
