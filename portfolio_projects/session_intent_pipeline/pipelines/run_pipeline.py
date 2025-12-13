# pipelines/run_pipeline.py

import pandas as pd

from feature_store.sessionizer import Sessionizer
from feature_store.aggregator import SessionTextAggregator


def main():
    print("INFO: Session Intent Pipeline started")

    # ====================
    # Load raw data
    # ====================
    df = pd.read_csv("data/raw/raw_events.csv")
    df["event_time"] = pd.to_datetime(df["event_time"])

    print(f"Loaded raw events: {len(df)} rows")

    # ====================
    # Sessionization (Day1)
    # ====================
    sessionizer = Sessionizer(inactivity_minutes=30)
    df_sessions = sessionizer.assign_sessions(df)

    print("Sessionization completed")
    print(df_sessions[["user_id", "event_time", "session_id"]].head())

    total_sessions = df_sessions.groupby(["user_id", "session_id"]).ngroups
    print("Total sessions:", total_sessions)

    # ====================
    # Session-level text aggregation (Day2)
    # ====================
    aggregator = SessionTextAggregator(text_col="event_text")
    session_docs = aggregator.aggregate(df_sessions)

    print("Session-level aggregation completed")
    print(session_docs.head())
    print("Number of session documents:", len(session_docs))


if __name__ == "__main__":
    main()
