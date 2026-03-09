# Analysis of Migraine MMDs: Anti-CGRP Effectiveness
This project evaluates the long-term effectiveness of anti-CGRP monoclonal antibodies in 179 migraine patients. The study focuses on handling high attrition rates in longitudinal medical data and identifying distinct patient responder phenotypes.

## Key Highlights
- **Dataset**: 179 patients, 3-year longitudinal study (3 treatment cycles).

- **Data Strategy**: Addressed patient drop-out using MICE (Multivariate Imputation by Chained Equations) and LOCF for robust statistical inference.

- **Modeling**: Implemented Mixed-Effect Models to account for within-patient variability and nested data structures.

- **Primary Outcome**: Median Monthly Migraine Day (MMD) reduction improved from 57% (Cycle 1) to ~70% (Cycle 3).

## Patient Phenotypes (Clustering)
Using temporal pattern analysis, patients were stratified into three clinical clusters:

- Cluster 0 (**Responders**): High stability, low MMDs, and 0% discontinuation rate.

- Cluster 1 (**Fluctuating**): High early volatility and treatment failure (85.9% discontinuation).

- Cluster 2 (**Partial Responders**): Gradual but significant improvement, despite complex clinical histories.

## Tech Stack & Methods
- **Language**: Python (Pandas, Statsmodels, Scikit-learn).

- **Statistical Methods**: Kruskal-Wallis tests (clinical history vs. demographics), Mixed-Effects Modeling.

- **Feature Engineering**: MICE for longitudinal data imputation.

----

### Repository Content
- **Migraine_Analysis.ipynb**: Full pipeline from EDA to clustering and modeling.

- **MigraineAnalysisReport.pdf**: Comprehensive statistical report and clinical discussion.

- **MigraineAnalysisPresentation.pdf**: Visual summary of the study and key findings.
