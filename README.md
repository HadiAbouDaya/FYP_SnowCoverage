# FYP_SnowCoverage

# AI-Driven Snow Coverage Analysis Project

## Overview
This repository documents our AI-driven project aimed at analyzing snow coverage. We detail our iterative process, challenges faced, and the improvements made in each iteration.

## Iterations
### First Iteration: [`FYP_SnowCoverage/AI_SnowCoveredArea/trainScfDNN.ipynb`](https://github.com/HadiAbouDaya/FYP_SnowCoverage/blob/main/AI_SnowCoveredArea/trainScfDNN.ipynb)
#### Data Loading
- Systematic data loading and processing using Python and pandas.
- Conversion of Day of Year indices to datetime format.
- Stacking dates and snow cover fractions into a single DataFrame.
- Adjustment to Uerra convention and streamlining the DataFrame.

#### Data Exploration
- Dissecting dataset to understand its composition.
- Identifying patterns, correlations, and potential outliers.
- Guiding analytical strategies and feature engineering.
- Employing statistical summaries and visualization techniques.

### Second Iteration: [`FYP_SnowCoverage/AI_SnowCoveredArea/trainScfSeq2Seq.ipynb`](https://github.com/HadiAbouDaya/FYP_SnowCoverage/blob/main/AI_SnowCoveredArea/trainScfSeq2Seq.ipynb)
- Utilization of a more intricate LSTM architecture.
- Continued focus on addressing data generalization challenges.

### Third Iteration: [`FYP_SnowCoverage/LebanonDataModeling_Prediction/trainScfLSTM_GRU.ipynb`](https://github.com/HadiAbouDaya/FYP_SnowCoverage/blob/main/LebanonData-Modeling_Prediction/trainScfLSTM_GRU.ipynb)
- Similar data loading and exploration as previous iterations.
- Implementation of data imputation and interpolation techniques.
- Application of detrending techniques for quality enhancement.

### Fourth Iteration: [`FYP_SnowCoverage/Pretrain_AlpsData/pretrainTS_alpsPrediction.ipynb`](https://github.com/HadiAbouDaya/FYP_SnowCoverage/blob/main/Pretrain_AlpsData/pretrainTS_alpsPrediction.ipynb)
- Pretraining models on the French Alps dataset.
- Modified LSTM architecture based on hyperparameter tuning.

### Fifth Iteration: [`FYP_SnowCoverage/LebanonData-Finetuning_Prediction/fine-tuneLbData_Prediction.ipynb`](https://github.com/HadiAbouDaya/FYP_SnowCoverage/blob/main/LebanonData-Finetuning_Prediction/fine-tuneLbData_Prediction.ipynb)
- Adoption of a transfer learning approach.
- Repurposing the model trained on the French Alps dataset.

## Model Evaluation
- Utilization of the Nash-Sutcliffe Efficiency (NSE) as the primary metric.
- Comparison of NSE scores across different experimental types.
  - Conventional training: 0.825
  - Pretraining on French Alps dataset: 0.8729
  - Transfer learning on Lebanese data: 0.859

## Figures and Results
- Detailed figures showcasing various stages of data processing and model evaluations.
- In-depth analysis of the predictive accuracy of different models.

## Conclusion
This project demonstrates the application of AI and machine learning in environmental data analysis, particularly in studying snow cover dynamics. It emphasizes the importance of iterative improvements and the effective use of techniques like transfer learning in climatological studies.

---

For detailed analysis and results, refer to individual Jupyter notebooks in this repository.
