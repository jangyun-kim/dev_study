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

## Version: v1.4

### Version Management

- MAJOR (예: v1.0.0 → v2.0.0)
  대규모 구조 변경 시 발생한다:

  - 템플릿/폴더 구조 자체가 바뀔 때
  - Daily Project 생성 로직이 완전히 재설계될 때
  - 이전 버전과 호환이 깨지는 변경이 있을 때

**예시**

- 프로젝트 생성 구조가 pipelines → src 구조로 완전히 전환됨
- SQL/Notebook/Python 템플릿 구성이 완전히 새롭게 바뀜
- create_project.py 실행 파라미터가 변경됨

- MINOR (예: v1.2.0 → v1.3.0)
  **새로운 기능을 추가했을 때 적용되는 업데이트:**
- 템플릿에 notebook 추가
- SQL 기본 분석 템플릿 추가
- Feature Engineering 샘플 추가
- 테스트 템플릿 강화
- 문서 자동 생성 기능 확장
  호환성은 유지되며, MAJOR 업데이트 없이 기능만 강화됨

- PATCH (예: v1.2.1 → v1.2.2)
  **버그 수정** 또는 **작은 품질 개선** 시 적용:
- 경로 문제 해결
- 오타 수정
- create_project.py 리팩토링
- 템플릿 내부 변수 누락 fix
  기능적 변화 없이 동작 안정성을 높이는 목적.

### Version History

| Version    | Date       | Changes                                       |
| ---------- | ---------- | --------------------------------------------- |
| **v1.4.0** | 2025-12-09 | Change Log System Added & Version Unification |
| **v1.3.0** | 2025-12-08 | Unified Version System                        |
| **v1.2.0** | 2025-12-08 | Notebook + Feature/SQL Templates Added        |
| **v1.1.0** | 2025-12-08 | Full Template System                          |
| **v1.0.0** | 2025-12-07 | Initial Generator                             |

### Version Change Log

- **v1.4.0 (2025-12-09)**:
  - Daily Version 제거 및 Global Version 단일화,
  - create_project.py 내부 Change Log 공식 섹션 추가,
  - README에 Template Version 자동 삽입 로직 통합
  - 전체 버전 관리 체계 정립 (MAJOR/MINOR/PATCH)
- **v1.3.0 (2025-12-08)**: ModelInputBuilder class skeleton 추가
  - Daily project versions removed
  - Only global template version maintained as general version
  - Daily README cleanup & version removal
- **v1.2.0 (2025-12-08)**: Notebook template & diagram template 자동생성 기능 추가
  - Notebook template 자동 생성
  - Feature engineering sample 추가
  - SQL analysis 치환 기능 구축
- **v1.1.0 (2025-12-08)**:
  - Python / SQL / Markdown / Tests 템플릿 구조 완성
  - placeholder 치환 기능 구축
- **v1.0.0 (2025-12-07)**:
  - 기본 project_YYYY-MM-DD 자동 생성 기능 구축
  - pipeline / builder / evaluator / tests 기본 생성

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
