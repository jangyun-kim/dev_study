"""
Auto EDA Module (Lightweight)
First added v1.5
============================================================

Automatically generates:
- data types summary
- missing value summary
- numeric distributions
- correlation heatmap

Output:
- assets/eda_overview.md

This module keeps EDA lightweight without large dependencies.
============================================================
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AutoEDA:
    """
    Lightweight Auto EDA generator
    """

    def __init__(self, output_dir="assets"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def run(self, df: pd.DataFrame):
        """
        Generate EDA report:
        - md report
        - distributions
        - correlation heatmap
        """
        report_path = os.path.join(self.output_dir, "eda_overview.md")

        with open(report_path, "w", encoding="utf-8") as f:

            f.write("# Auto EDA Overview\n\n")

            # ---- Data Types ----
            f.write("## Data Types\n")
            f.write(df.dtypes.to_markdown())
            f.write("\n\n")

            # ---- Missing Values ----
            f.write("## Missing Values\n")
            f.write(df.isna().sum().to_markdown())
            f.write("\n\n")

            # ---- Basic Statistics ----
            f.write("## Basic Stats\n")
            f.write(df.describe(include='all').to_markdown())
            f.write("\n\n")

        # ---- Visualizations ----
        numeric_cols = df.select_dtypes(include='number').columns

        # numeric distribution
        for col in numeric_cols:
            plt.figure(figsize=(6, 3))
            sns.histplot(df[col], kde=True)
            plt.title(f"Distribution of {col}")
            plt.savefig(os.path.join(self.output_dir, f"dist_{col}.png"))
            plt.close()

        # correlation heatmap
        if len(numeric_cols) > 1:
            plt.figure(figsize=(6, 5))
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="Blues")
            plt.title("Correlation Heatmap")
            plt.savefig(os.path.join(self.output_dir, "correlation_heatmap.png"))
            plt.close()

        print(f"[AutoEDA] Report generated: {report_path}")
