# User Behavior Intelligence Project

### Session-based Analytics → Intent Modeling → ML/DL Prediction

---

## 1. Project Overview

이 프로젝트는 **Raw User Event Log**로부터 출발하여,  
세션 단위 데이터 모델링 → 사용자 의도(Intent) 추론 →  
머신러닝/딥러닝 기반 분석까지 단계적으로 확장하는  
**장기 실무형 데이터 분석 프로젝트**입니다.

> 단발성 과제가 아닌,  
> **실제 서비스 환경에서 데이터 분석가/ML 엔지니어가 수행하는 전체 흐름을 재현**하는 것을 목표로 합니다.

---

## 2. Why This Project Matters

실무에서 데이터 분석/ML 프로젝트는 보통 다음과 같은 구조를 가집니다.

1. 데이터가 지저분한 상태로 들어온다 (Raw Logs)
2. 바로 모델을 쓰면 성능도 해석도 모두 망가진다
3. **문제는 모델이 아니라 데이터 구조**
4. 세션, 집계, Feature Engineering이 프로젝트 성패를 좌우한다

이 프로젝트는  
👉 **“모델 이전 단계의 데이터 설계 능력”**을 가장 중요하게 다룹니다.

---

## 3. End-to-End Project Scope

본 프로젝트는 아래 단계를 순차적으로 진행합니다.

### Phase 1. Session-based Data Modeling

- Raw event log → Sessionization
- Inactivity gap 기반 세션 분리
- Session-level 데이터 구조 설계

### Phase 2. Session Feature Engineering

- Session text aggregation
- Count / time / diversity feature 생성
- Feature Store 구조 설계

### Phase 3. Intent Representation

- TF-IDF / Embedding 기반 벡터화
- Dimensionality reduction (PCA / UMAP)
- Session intent clustering

### Phase 4. Machine Learning

- Session intent classification
- User behavior pattern prediction
- Feature importance 분석

### Phase 5. Deep Learning (Optional Extension)

- Sequence modeling (LSTM / Transformer)
- Session sequence 기반 next-action prediction

---

## 4. Long-term Roadmap (Daily Progress Plan)

> **원칙**
>
> - 매일 프로젝트의 “다음 자연스러운 한 단계”만 진행
> - 구조는 고정, 내용만 누적
> - 하루에 끝내지 않고, 이해를 쌓는 방식

---

### Week 1 — Data Modeling & Sessionization

| Day   | Focus                           | detail                                                                                                                                                                                                                               |
| ----- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Day 1 | Raw Event 이해 & Sessionization | - Defined session boundaries based on inactivity threshold <br /> - Implemented reusable `Sessionizer` class <br /> - Validated session counts and edge cases                                                                        |
| Day 2 | Session-level Text Aggregation  | Event-level user logs were aggregated into session-level documents, preserving temporal order.<br  /> Each session represents a coherent user intent window and serves as the fundamental document unit for downstream NLP modeling. |

| Day 3 | Session-level Feature Engineering | Session documents were transformed into TF-IDF vectors using unigram and bigram features.<br /> This representation enables intent clustering and similarity analysis at the session level. |
| Day 4 | Feature Store 구조 고도화 |
| Day 5 | SQL 기반 세션 집계 버전 구현 |

---

### Week 2 — Intent Representation

| Day    | Focus                 |
| ------ | --------------------- |
| Day 6  | TF-IDF Vectorization  |
| Day 7  | Embedding Shape 해석  |
| Day 8  | PCA / UMAP 시각화     |
| Day 9  | Intent Clustering     |
| Day 10 | Cluster 해석 & Naming |

---

### Week 3 — Machine Learning

| Day    | Focus                           |
| ------ | ------------------------------- |
| Day 11 | Intent Classification 문제 정의 |
| Day 12 | Feature Selection               |
| Day 13 | Model Training (Baseline)       |
| Day 14 | Evaluation & Error Analysis     |
| Day 15 | Business Interpretation         |

---

### Week 4 — Advanced / DL Extension (Optional)

| Day    | Focus                        |
| ------ | ---------------------------- |
| Day 16 | Session Sequence Modeling    |
| Day 17 | LSTM 기반 행동 예측          |
| Day 18 | Attention / Transformer 개념 |
| Day 19 | 결과 비교                    |
| Day 20 | Final Report 정리            |

---

## 5. Project Structure

```bash
portfolio_projects/
└── user_behavior_intelligence/
├── data/
│ ├── raw/
│ └── processed/
├── feature_store/
│ ├── sessionizer.py
│ ├── text_aggregator.py
│ └── feature_builder.py
├── models/
│ ├── vectorizer.py
│ └── classifier.py
├── pipelines/
│ └── run_pipeline.py
├── notebooks/
│ ├── analysis.ipynb
│ └── visualization.ipynb
└── README.md
```

---

## 6. How I Use This Project (Learning Strategy)

- GitHub:
  - 코드 + 구조 + 실행 가능한 파이프라인
- Notion:
  - Day별 학습 노트
  - 개념 정리
  - “왜 이렇게 설계했는지” 사고 기록
- 목표:
  - **한 프로젝트를 반복해서 깊게 파는 경험**
  - 새로운 프로젝트를 만들지 않고, 기존 프로젝트를 진화시킴

---

## 7. Key Takeaway

> 좋은 데이터 분석가는  
> **모델을 잘 쓰는 사람이 아니라,  
> 모델이 잘 작동하도록 데이터를 설계하는 사람이다.**

---

## 8. Next Step (Today’s Progress)

- [x] Sessionization pipeline 구축
- [ ] Session-level text aggregation
- [ ] Feature engineering 확장

## 2. Tech Stack

- Python
- Pandas / NumPy
- Scikit-learn
- Jupyter Notebook
- Git / GitHub

---

## 3. Project Structure

```bash
session_intent_pipeline/
├── data/ # raw & processed data
├── feature_store/ # reusable feature engineering logic
├── pipelines/ # executable pipelines
├── models/ # ML models & embeddings
├── notebooks/ # exploratory analysis
└── README.md
```

---

## 4. Progress Log

### Day 1 – Sessionization

## Day 2 – Session-level Text Aggregation

### Day 3 – Vectorization & Intent Representation

- TF-IDF based session embeddings
- Dimensionality inspection & validation
