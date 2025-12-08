import sys, os
sys.path.append(os.getcwd())

import pandas as pd
from feature_store.user_features import UserFeatures
from feature_store.item_features import ItemFeatures

if __name__ == "__main__":
    print("🔵 Day3 Feature Store Pipeline started...")

    # 1) Load data
    df = pd.read_csv("data/events.csv", parse_dates=["timestamp"])

    # 2) Feature creators
    uf = UserFeatures()
    ife = ItemFeatures()

    # 3) Transform
    user_df = uf.transform(df)
    item_df = ife.transform(df)

    # 4) Save
    user_df.to_csv("data/user_features.csv", index = False)
    item_df.to_csv("data/item_features.csv", index = False)

    print("Feature Store build completed!")
    print("Saved files:")
    print("- data/user_features.csv")
    print("- data/item_features.csv")
