# Session-based User Intent Modeling Pipeline

## 1. Project Overview

This project builds an end-to-end data pipeline that transforms raw user
event logs into session-level intent representations for downstream analytics
and machine learning tasks.

The goal is to simulate a real-world data platform workflow:
raw logs → feature engineering → modeling → interpretation.

---

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

- Defined session boundaries based on inactivity threshold
- Implemented reusable `Sessionizer` class
- Validated session counts and edge cases

### Day 2 – Session-level Text Aggregation

- Aggregated event text into session-level documents
- Built clean text pipeline for downstream modeling
- Verified session document integrity

(Next)

### Day 3 – Vectorization & Intent Representation

- TF-IDF based session embeddings
- Dimensionality inspection & validation
