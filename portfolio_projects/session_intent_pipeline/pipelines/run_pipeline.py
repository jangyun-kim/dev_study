# pipelines/run_pipeline.py
import pandas as pd
from feature_store.sessionizer import Sessionizer

if __name__ == "__main__":
    print("INFO: Day1 pipeline started")

    df = pd.read_csv("data/raw/raw_events.csv")
    df["event_time"] = pd.to_datetime(df["event_time"])

    sessionizer = Sessionizer(inactivity_minutes = 30)
    df_sessions = sessionizer.assign_sessions(df)

    print(df_sessions[["user_id", "event_time", "session_id"]])
    print("총 세션 수: ", df_sessions.groupby(["user_id", "session_id"]).ngroups
)
