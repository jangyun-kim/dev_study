"""
============================================================
                Daily Project — Pipeline Template
============================================================
This file is auto-generated from templates/python/pipeline_template.py
You must implement the marked sections:

    # ====================================================
    #                 Fill your code
    # ====================================================

This template enforces:
- Modular class-based design
- Logging
- Clear data-flow separation (load → transform → evaluate → save)
============================================================
"""

import logging
from datetime import datetime
from builder.dataset_builder import DatasetBuilder
from evaluator.model_evaluator import ModelEvaluator

logger = logging.getLogger(__name__)


class DailyPipeline:
    """
    Main pipeline orchestrator for daily task.
    """

    def __init__(self):
        self.date = datetime.now().strftime("%Y-%m-%d")

    def run(self):
        logger.info(f"[Pipeline] Starting pipeline for {self.date}")

        # ====================================================
        #                 Fill your code (Load Data)
        #  Example:
        #  df = builder.load("data/raw.csv")
        # ====================================================
        builder = DatasetBuilder()
        df = builder.load()

        # ====================================================
        #                 Fill your code (Transform)
        # ====================================================
        transformed = builder.transform(df)

        # ====================================================
        #                 Fill your code (Evaluation)
        # ====================================================
        evaluator = ModelEvaluator()
        result = evaluator.evaluate(transformed)

        logger.info("[Pipeline] Completed.")
        return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    pipeline = DailyPipeline()
    pipeline.run()
