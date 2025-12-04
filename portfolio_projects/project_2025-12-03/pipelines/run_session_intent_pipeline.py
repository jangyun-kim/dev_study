import os, sys
PROJECT_ROOT = r"G:\My Drive\MyPortfolio\dev_study\portfolio_projects\project_2025-12-03"
sys.path.insert(0, PROJECT_ROOT)


import logging
import pandas as pd
from feature_store.sessionizer import Sessionizer
from feature_store.vectorizer import SessionVectorizer
from feature_store.clusterer import IntentClusterer

df = pd.read_csv("data/raw_events.csv", skip_blank_lines=True)
df = df.dropna(how="all")   # 빈 줄 제거(전체 NaN 행)
df["event_time"] = pd.to_datetime(df["event_time"])


if __name__ == "__main__":
    """
    전체 Pipeline의 지휘자 역할
    → Data Engineer 프로젝트에 매우 중요한 구조
    """
    logging.basicConfig(level=logging.INFO)
    logging.info("Day1 Pipeline started.")

    # 1) Load raw data
    df = pd.read_csv("data/raw_events.csv")
    df["event_time"] = pd.to_datetime(df["event_time"])

    # 2) Sessionize
    sessionizer = Sessionizer(inactivity_minutes=30)
    df = sessionizer.assign_sessions(df)

    # 3) Session text aggregation
    session_texts = df.groupby(["user_id", "session_id"])["event_text"].apply(lambda x: " ".join(x))


    # 4) Vectorize
    vectorizer = SessionVectorizer()
    X = vectorizer.fit_transform(session_texts)

    # 5) Cluster
    clusterer = IntentClusterer(k=8)
    labels = clusterer.fit_predict(X)

    # 6) Save result
    result = pd.DataFrame({
        "session_id": session_texts.index,
        "intent_cluster": labels
    })
    result.to_csv("data/session_intents.csv", index=False)

    logging.info("Day1 Pipeline completed.")

    print(session_texts.index)
    print(labels[:10]) 

