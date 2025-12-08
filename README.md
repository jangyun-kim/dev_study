# Data Portfolio – Practical Machine Learning & Data Engineering Projects

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

## Version History

| Version    | Date       | Changes                                                   |
| ---------- | ---------- | --------------------------------------------------------- |
| **v0.1.0** | 2025-12-02 | 프로젝트 구조 설계, Day1 Sessionizer 개발                 |
| **v0.2.0** | 2025-12-03 | Clusterer 추가, Feature Store 설계                        |
| **v0.3.0** | 2025-12-04 | README 구조 개선, Day3 Feature Engineering 완료           |
| **v0.4.0** | 2025-12-05 | create_project.py 전면 개편 (자동 프로젝트 생성기 고도화) |
| **v0.4.1** | 2025-12-05 | Template 기반 생성, 불필요 폴더 제거                      |
| **v0.5.0** | 2025-12-06 | Day4 DE Pipeline 설계를 위한 구조 추가                    |

### Version

- **v0.1.0 (2025-12-09)**: 초기 템플릿 생성, Session-level Aggregation Task 정의
- **v0.1.1 (2025-12-09)**: ModelInputBuilder class skeleton 추가
- **v0.1.2 (2025-12-09)**: Notebook template & diagram template 자동생성 기능 추가

---

## Repository Structure

아래는 전체 프로젝트 구조입니다:

```bash
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
```

---

## Project Archive (자동 확장 구조)

프로젝트는 날짜별로 `portfolio_projects/project_YYYY-MM-DD/` 폴더에 누적됩니다.
각 프로젝트는 독립 실행 가능한 상태로 설계되어 있으며,
해당 폴더 내 `README.md`를 통해 상세 내용을 확인할 수 있습니다.

예시:

```bash
portfolio_projects/
├── project_2025-12-03/ # Day1
├── project_2025-12-04/ # Day2
├── project_2025-12-05/ # Day3
└── ...
```

---

## How to Create a New Project

아래 스크립트를 사용하여 새 프로젝트 폴더를 생성합니다:

```bash
python tools/create_project.py --date YYYY-MM-DD
```

생성된 폴더는 다음을 포함합니다:

• 데이터 폴더
• feature_store 모듈
• pipelines 실행 스크립트
• 테스트 파일
• 템플릿 README

---

## Development Principles

• 기능별 모듈화
(feature_store/sessionizer.py, vectorizer.py, clusterer.py 등)

• 파이프라인 기반 실행
(pipelines/run_xxx.py)

• 테스트 기반 안정성 확보
(pytest로 모든 주요 함수 검증)

• 데이터 구조 & 코드 구조의 일관성 유지

---

## Running Tests

pytest

---

## Purpose

본 포트폴리오는 일반적인 B2C/B2B 서비스 환경에서 사용되는 행동 분석 및 ML Pipeline 설계 역량을 입증하는 것을 목표로 합니다.

---

### Developer Notes

- v0.4.1에서 create_project.py를 개선하며 templates 기반 구조로 이동함.
  이전 버전은 매일 동일한 폴더 구조를 생성했으나, Day별로 필요한 파일이 달라지므로
  유지보수성이 떨어지는 문제를 해결함.
- Day4부터 Notebook 시각화 assets 폴더를 각 프로젝트 내부로 이동하여
  프로젝트 독립성이 강화됨.
