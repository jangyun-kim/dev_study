import pandas as pd

class UserFeatures:
    """사용자 단위 Feature 생성"""

    def __init__(self):
        pass

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """user-level aggregation features"""

        # 전체 이벤트 수
        total_events = df.groupby("user_id").size().rename("user_total_events")

        # 고유 아이템 수
        unique_items = df.groupby("user_id")["item_id"].nunique().rename("user_unique_items")

        # 클릭 수
        click_count = (
            df[df["is_click"] == 1]
            .groupby("user_id")
            .size()
            .rename("user_clicks")
        )

        # merge
        user_features = pd.concat([total_events, unique_items, click_count], axis=1).fillna(0)
        user_features.reset_index(inplace=True)
        return user_features
