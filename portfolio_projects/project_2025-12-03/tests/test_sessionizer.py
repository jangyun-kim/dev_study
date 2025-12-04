import pandas as pd
from feature_store.sessionizer import Sessionizer

def test_session_split():
    # ============================
    #            Fill your code
    # ============================

    df = pd.DataFrame({
        "user_id": [1,1],
        "event_time": ["2025-01-01 10:00", "2025-01-01 11:00"],
        "event_text": ["view", "click"]
    })
    df["event_time"] = pd.to_datetime(df["event_time"])

    s = Sessionizer(inactivity_minutes=30)
    out = s.assign_sessions(df)

    assert out["session_id"].nunique() == 2
