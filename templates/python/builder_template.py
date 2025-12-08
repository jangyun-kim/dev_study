"""
Dataset Builder Template
============================================================
Responsible for:
- Data loading
- Preprocessing
- Feature engineering

샘플 Feature Engineering 포함 (현업 빈출):
  1) 결측값 처리
  2) type casting
  3) datetime 파싱
  4) 간단한 파생변수 생성
  5) 범주형 인코딩 기초
============================================================
"""

import pandas as pd
import logging

logger = logging.getLogger(__name__)


class DatasetBuilder:

    def load(self):
        logger.info("[Builder] Loading dataset...")

        # ====================================================
        #  Sample: 기본 구조 — 직접 dataset 경로를 입력해야 합니다.
        # ====================================================
        # df = pd.read_csv("data/raw_events.csv")
        # return df

        # ====================================================
        #                 Fill your code
        # ====================================================
        raise NotImplementedError("Implement dataset loading")

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("[Builder] Transforming dataset...")

        # 🟦 샘플 Feature Engineering (삭제/수정 가능)
        # ------------------------------------------------

        # 1) datetime 변환
        if "event_time" in df.columns:
            df["event_time"] = pd.to_datetime(df["event_time"])

        # 2) 결측값 처리 (샘플)
        df = df.fillna({
            "event_text": "unknown",
        })

        # 3) 문자열 카테고리 처리
        if "event_text" in df.columns:
            df["event_text"] = df["event_text"].astype("category")

        # 4) 길이 파생변수 예시
        if "event_text" in df.columns:
            df["text_len"] = df["event_text"].astype(str).apply(len)

        # 5) 시간 기반 파생변수
        if "event_time" in df.columns:
            df["hour"] = df["event_time"].dt.hour

        # ------------------------------------------------
        # 👇 아래 영역은 오늘 프로젝트 수행자가 직접 작성해야 함
        # ====================================================
        #                 Fill your code
        # ====================================================
        raise NotImplementedError("Implement dataset transformation")

        return df
