# Day3 Project — User/Item Feature Store 구축

## 1) 프로젝트 개요 (Business Scenario)

현대차, 네이버, 카카오 등 대부분의 데이터 기반 기업은  
**사용자(User)와 아이템(Item)의 행동 로그를 정제하여 Feature Store를 구축한 뒤,  
추천 모델·개인화 서비스·A/B 테스트에서 재사용 가능한 특징(feature)을 안정적으로 제공하는 시스템**을 운영합니다.

본 Day3 프로젝트는 실제 기업에서 사용하는 구조를 간단한 형태로 재현하여,  
**User-level / Item-level Aggregated Feature Store 구축 능력**을 실습하는 것을 목표로 합니다.

---

## 2) 프로젝트 목표

### 핵심 목표

- 원본 이벤트 로그(`events.csv`)로부터  
  **사용자(User) Feature**와 **아이템(Item) Feature** 자동 생성
- 재사용 가능한 Feature Builder 클래스를 설계하여  
  향후 모델링 단계에서 바로 활용 가능한 구조 구축
- 파이프라인 실행 한 번으로 Feature Store 전처리 자동화

### 본 프로젝트로 입증되는 3가지 핵심 기술 역량

1. **Modular Code Design (클래스 기반 설계 능력)**
2. **Feature Engineering 능력 (aggregation, CTR, 클릭/조회 패턴 분석)**
3. **데이터 파이프라인 구축 능력 (Pipeline Architecture)**

---

## 3) 기술 스택 (Tech Stack)

| Category        | Tools                                     |
| --------------- | ----------------------------------------- |
| Language        | Python 3.9+                               |
| Data Processing | pandas, numpy                             |
| Pipeline        | Class-based Feature Builder Architecture  |
| Storage         | Local CSV-based Lightweight Feature Store |
| Version Control | Git, GitHub                               |

---

## 4) 구현 기능 상세 (Implementation Details)

### (1) User Feature Builder

`feature_store/user_features.py`

생성되는 사용자 단위 Feature:

- `user_total_events` : 총 이벤트 수
- `user_unique_items` : 고유 아이템 수
- `user_clicks` : 클릭 이벤트 수

사용된 기술:

- `groupby`, `size()`, `nunique()`, conditional filtering
- 결측치 처리 (`fillna(0)`)

### (2) Item Feature Builder

`feature_store/item_features.py`

생성되는 아이템 단위 Feature:

- `item_views` : 조회(view) 횟수
- `item_clicks` : 클릭(click) 횟수
- `item_ctr` : Click-Through Rate (CTR)

사용된 기술:

- 조회/클릭 이벤트 분리 처리
- CTR 계산 시 ZeroDivision 방지 처리
- Aggregation 기반 Feature Engineering

### (3) Feature Store Pipeline 자동화

`pipelines/build_feature_store.py`

동작:

- events.csv 로드
- User Features 생성 → 저장
- Item Features 생성 → 저장
- 모든 작업이 하나의 실행 파일에서 자동 처리됨

결과 파일:
data/user_features.csv
data/item_features.csv

---

## 5) 프로젝트 파일 구조

```markdown
project_2025-12-08/
│
├─ data/
│ ├─ events.csv
│ ├─ user_features.csv
│ └─ item_features.csv
│
├─ feature_store/
│ ├─ user_features.py
│ ├─ item_features.py
│ └─ init.py
│
├─ pipelines/
│ ├─ build_feature_store.py
│ └─ init.py
│
└─ README.md
```

---

## 6) 실행 방법 (Run Instructions)

### 1) 프로젝트 디렉토리 이동

```bash
cd project_2025-12-08
```

### 2) 파이프라인 실행

```bash
python pipelines/build_feature_store.py
```

### 3) 생성 결과 확인

```bash
data/user_features.csv
data/item_featrues.csv
```

## 7) Output 예시 (요약)

user_featrues.csv 예시

| user_id | user_total_events | user_unique_items | user_clicks |
| ------- | ----------------- | ----------------- | ----------- |
| 1       | 6                 | 2                 | 2           |
| 2       | 5                 | 2                 | 1           |
| 3       | 6                 | 2                 | 2           |

item_features.csv 예시

| item_id | item_views | item_clicks | item_ctr |
| ------- | ---------- | ----------- | -------- |
| 101     | 2          | 1           | 0.50     |
| 202     | 2          | 1           | 0.50     |
| 401     | 2          | 1           | 0.50     |

## 8) 기술적 포인트 (Technical Insight)

### Feature Store를 구성하는 이유

- 모델 입력 데이터 일관성 보장
- 실험/서비스 환경의 feature drift 방지
- 재사용 가능한 feature pipeline 구축 가능

### Groupby Aggregation의 핵심 이슈

- NA 처리
- ZeroDivision 방지
- 데이터 타입 유지
- Aggregation 후 merge 전략

### CTR 계산의 실무적 고려사항

- CTR = 클릭수 / 조회수
- 하지만 실무에서는:
  - 조회수 0일 때 division 방지 필요
  - Bot traffic 필터링
  - Time-decay 적용 가능

## 9) 면접 대비 기술 질문 (Interview Questions)

### Q1. Feature Store를 분리해두면 어떤 장점이 있습니까?

→ Serving/Training consistency 보장, 중복된 계산 감소, 재사용성 증가 등

### Q2. CTR(feature)을 계산할 때 발생할 수 있는 문제와 해결법은?

→ Zero division, bot traffic, extreme outliers 등 처리 전략 설명

## 10) 향후 확장 방향 (Next Steps)

- Session-based Features 추가
- Embedding 기반 Feature Store 구축
- Spark/BigQuery 기반 분산 Feature Store로 확장
- ML 모델 학습 파이프라인과 연결

---

Day3는 ‘기초적인 Feature Store 구축 능력’을 학습하는 단계이며,
Day4부터는 모델링과 더 깊은 데이터 파이프라인 설계로 확장될 예정입니다.
