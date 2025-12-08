# Day3 – Intent Classification with LightGBM

## Overview

세션 텍스트(TF-IDF)와 행동 통계(numeric features)를 결합하여  
LightGBM 기반 Multi-class Intent Classification 모델을 생성합니다.

## Project Structure

(폴더 구조 생략 가능)

## How to Run

```bash
python pipelines/run_training_pipeline.py
```

## Results

모델 저장: models/lightgbm_model.pkl

성능 지표: Accuracy / Macro F1(추가 예정)

## Test

```bash
pytest
```

## Future Work

Sentence-BERT 기반 embedding

Feature store 확장 설계

Hyperparameter optimization
