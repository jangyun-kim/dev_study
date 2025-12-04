# Day1 — Session & Intent Clustering Pipeline

## 1. Problem & Business Context

- **Goal**  
  Raw user event logs (`user_id`, `event_time`, `event_text`) 를 세션 단위로 분리하고,  
  각 세션의 텍스트를 기반으로 KMeans clustering 을 수행하여  
  유저의 행동 의도(intent)를 그룹화하는 파이프라인을 설계.

- **Scenario**
  - 현대자동차 커넥티드카 로그, 네이버/카카오 웹/앱 로그를 가정.
  - “한 세션 동안 사용자가 무엇을 하려 했는지”를 파악해 추천, 마케팅, 이탈 분석 등에 활용할 수 있는 기본 분석 인프라 구축.

## 2. Tech Stack

- Python 3.x
- pandas
- scikit-learn (TfidfVectorizer, KMeans)
- pytest
- Logging (built-in `logging` module)

## 3. Data

- `data/raw_events.csv`

  - Columns:
    - `user_id` (int)
    - `event_time` (str → datetime)
    - `event_text` (str)

- `data/session_intents.csv`
  - Session-level 결과 (세션 텍스트, TF-IDF 기반 클러스터 라벨 등)

## 4. Architecture

```text
feature_store/
  sessionizer.py   # user_id, event_time 기반 inactivity gap 로 session_id 지정
  vectorizer.py    # (user_id, session_id) 별 event_text → session text → TF-IDF
  clusterer.py     # KMeans 로 세션 intent clustering

pipelines/
  run_session_intent_pipeline.py
    - raw_events.csv 로드
    - sessionizer.assign_sessions()
    - session_texts 생성
    - vectorizer.fit_transform()
    - clusterer.fit_predict()
    - session_intents.csv 저장

tests/
  test_feature_store.py  # sessionizer / vectorizer / clusterer 유닛 테스트
```
