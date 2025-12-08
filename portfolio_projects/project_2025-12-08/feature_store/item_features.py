import pandas as pd

class ItemFeatures:
    """아이템 단위 Feature 생성"""

    def __init__(self):
        pass

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """item-level aggregation features"""

        # 전체 조회 횟수
        total_views = df[df["event"] == "view"].groupby("item_id").size().rename("item_views")

        # 클릭 횟수
        total_clicks = df[df["event"] == "click"].groupby("item_id").size().rename("item_clicks")

        # CTR 계산
        item_features = pd.concat([total_views, total_clicks], axis=1).fillna(0)
        item_features["item_ctr"] = item_features["item_clicks"] / item_features["item_views"].replace(0, 1)

        item_features.reset_index(inplace=True)
        return item_features
