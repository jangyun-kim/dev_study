# Session Intent Analysis Pipeline

## Overview

This project builds an end-to-end NLP pipeline that transforms raw user
event logs into session-level intent clusters.

## Pipeline

1. Sessionization (time-based)
2. Session-level text aggregation
3. TF-IDF vectorization
4. KMeans clustering
5. Cluster interpretation

## Tech Stack

- Python
- pandas, scikit-learn
- TF-IDF, KMeans

## How to Run

```bash
python -m pipelines.run_pipeline
```

## Result

- Session-level intent clusters identified
- Interpretable keyword-based intent descriptions

## Project Structure

feature_store/
pipelines/
notebooks/
data/

## Key Learnings

- Session is a more meaningful unit than individual events
- Composite keys prevent session collisions
- Text representation choice affects clustering quality

---

```markdown
This project emphasizes pipeline design, reproducibility, and interpretability rather than model complexity.
```
