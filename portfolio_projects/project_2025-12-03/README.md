## 📄 **`project_2025-12-03/README.md`**

`````markdown
# Day1 – Session & Intent Clustering Pipeline

## 1. Overview

웹/앱 사용자 행동 로그(raw events)를 기반으로 세션을 분리(Sessionization)하고,
세션 내 텍스트 이벤트를 TF-IDF 기반 벡터로 변환하여
KMeans로 세션 의도(Intent)를 군집화하는 기본 ML 파이프라인을 구현합니다.

---

## 2. Business Context

일반적인 서비스 환경에서는 사용자 행동이 다음과 같이 기록됩니다:

- user_id
- event_time
- event_text

핵심 문제:

- “한 사용자가 한 세션 동안 무엇을 하려 했는가?”
- 세션의 목적(Intent)을 자동으로 파악할 수 있는가?

본 프로젝트는 이를 해결하는 **세션 기반 텍스트 분석 파이프라인**을 구현합니다.

---

## 3. Architecture

```markdown
project_2025-12-03/
│
├── data/
│ ├── raw_events.csv
│ └── session_intents.csv
│
├── feature_store/
│ ├── sessionizer.py
│ ├── vectorizer.py
│ └── clusterer.py
│
├── pipelines/
│ └── run_session_intent_pipeline.py
│
├── tests/
│ └── test_feature_store.py
│
└── README.md
```

---

## 4. Methods

### 4.1 Sessionization

- 이벤트 시간 기준 정렬
- 이전 이벤트와 시간 차 계산
- 30분 inactivity → 새 세션
- 세션 고유 ID = (`user_id`, `session_id`)

### 4.2 Vectorization (TF-IDF)

- 세션 내 텍스트를 하나의 문장으로 합침
- `TfidfVectorizer`로 의미 기반 고차원 벡터 생성

### 4.3 Clustering (KMeans)

- 세션을 의미 흐름에 따라 자동 군집화
- cluster label을 session-level 데이터에 저장

---

## 5. How to Run

### 1) Run Pipeline

```bash
python pipelines/run_session_intent_pipeline.py
```

```

```
`````

1. Output

data/session_intents.csv
→ 세션 텍스트 + TF-IDF feature + cluster label

1. Testing
   pytest

Sessionization 로직

벡터화 테스트

클러스터링 결과 shape 검증

1. Key Learnings

session_id는 user별 local index이므로
세션 고유 식별은 (user_id, session_id) 조합이어야 함

Blank row, dtype mismatch, clustering sample 부족 등
실무형 오류 디버깅 경험

기능별 모듈 구성(feature_store 구조)과
pipeline 구조 확립

1. Future Work

Sentence-BERT 임베딩 도입

세션 행동 통계 + 텍스트 임베딩 → Hybrid Clustering

사용자 Segment profiling 자동화
