# 📊 Data Portfolio – Practical Machine Learning & Data Engineering Projects

이 레포지토리는 웹/앱 기반 서비스 환경에서 수집되는 **사용자 행동 데이터(User Behavior Logs)** 를 활용하여  
Session Analysis → Feature Engineering → NLP Embedding → ML Pipeline 구축까지  
실무형 데이터 프로젝트를 체계적으로 수행하는 포트폴리오입니다.

프로젝트는 날짜별로 독립된 구조로 구성되며,  
각 프로젝트는 다음 원칙에 따라 진행됩니다:

- **실무 중심 문제 정의 (Business Scenario 기반)**
- **모듈형 코드 구조(Class-based Architecture)**
- **Feature Store 중심 데이터 엔지니어링**
- **재현 가능한 ML 파이프라인 설계**
- **Unit Test 기반 개발(Test-driven Development)**

---

## 📁 Repository Structure

아래는 전체 프로젝트 구조입니다:
dev_study/
│
├── portfolio_projects/
│ ├── project_YYYY-MM-DD/
│ │ ├── data/
│ │ ├── feature_store/
│ │ ├── pipelines/
│ │ ├── tests/
│ │ └── README.md
│ └── (다음 프로젝트들이 날짜별로 추가됩니다)
│
├── templates/
│ └── daily_project_template/
│
├── tools/
│ └── create_project.py
│
└── assets/
├── images/
└── references/

---

## 📈 Project Archive (자동 확장 구조)

프로젝트는 날짜별로 `portfolio_projects/project_YYYY-MM-DD/` 폴더에 누적됩니다.  
각 프로젝트는 독립 실행 가능한 상태로 설계되어 있으며,  
해당 폴더 내 `README.md`를 통해 상세 내용을 확인할 수 있습니다.

예시:
portfolio_projects/
├── project_2025-12-03/ # Day1
├── project_2025-12-04/ # Day2
├── project_2025-12-05/ # Day3
└── ...

※ 최상단 README는 매일 수정할 필요 없이, 프로젝트는 폴더 구조가 자동으로 확장됩니다.

---

## 🚀 How to Create a New Project

아래 스크립트를 사용하여 새 프로젝트 폴더를 생성합니다:

````bash
python tools/create_project.py --date YYYY-MM-DD

생성된 폴더는 다음을 포함합니다:

• 데이터 폴더
• feature_store 모듈
• pipelines 실행 스크립트
• 테스트 파일
• 템플릿 README

🛠 Development Principles

• 기능별 모듈화
(feature_store/sessionizer.py, vectorizer.py, clusterer.py 등)

• 파이프라인 기반 실행
(pipelines/run_xxx.py)

• 테스트 기반 안정성 확보
(pytest로 모든 주요 함수 검증)

• 데이터 구조 & 코드 구조의 일관성 유지

🧪 Running Tests
pytest

📌 Purpose
본 포트폴리오는 일반적인 B2C/B2B 서비스 환경에서 사용되는 행동 분석 및 ML Pipeline 설계 역량을 입증하는 것을 목표로 합니다.


---

# 🟦 (2) Day1 프로젝트 README – 완전 정제된 최종 버전 (Markdown 통일)

아래 내용은 `portfolio_projects/project_2025-12-03/README.md`에 넣으면 됨.

---

## 📄 **`project_2025-12-03/README.md`**

```markdown
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
2) Output

data/session_intents.csv
→ 세션 텍스트 + TF-IDF feature + cluster label

6. Testing
pytest


Sessionization 로직

벡터화 테스트

클러스터링 결과 shape 검증

7. Key Learnings

session_id는 user별 local index이므로
세션 고유 식별은 (user_id, session_id) 조합이어야 함

Blank row, dtype mismatch, clustering sample 부족 등
실무형 오류 디버깅 경험

기능별 모듈 구성(feature_store 구조)과
pipeline 구조 확립

8. Future Work

Sentence-BERT 임베딩 도입

세션 행동 통계 + 텍스트 임베딩 → Hybrid Clustering

사용자 Segment profiling 자동화
````
