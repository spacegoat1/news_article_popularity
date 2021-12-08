# Prediction of Online News Popularity
Project for the DATA1030 class at Brown University
Yash Mehta, Data Science Initiative
Supervised by Dr. Andras Zsom

## Goal
The goal of this project is to use various features of online news to predict its popularity (measured by the number of shares).

## Data
Dataset from UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/online+news+popularity.  
The dataset contains 59 features and the number of shares as target for 39644 pieces of news collected from Mashable.

## Modeling
The problem is modeled as a classification problem with a set threshold above which articles are considered to be popular. The threshold is set as the median of the number of shares. 
4 ML models were tested on the dataset:  
• Logistic Regression (without penalty, using L1 penalty and L2 penalty)
• K-Nearest Neighbors  
• Random Forest Classifier  
• XGBoost Classifier  

F-beta with beta = 1.5 was chosen as the evaluation metric. 

## Findings
• XGBoost was found to perform the best on the dataset with an F-beta values of 66.3%. 
• After model interpretation, the following factors were found to be most important to optimize for popularity:  
1. Keywords.  
2. Day of week of publication
3. References to other popular articles
4. Topic of the article

These observations are in line with general understanding of optimizing digital content. 

---
## Environment
Python version: `3.9.7`

Primary package versions:
`numpy==1.21.1`
`pandas==1.3.1`
`scikit-learn==0.24.2`
`shap==0.39.0`
`matplotlib==3.4.2`
`xgboost==1.3.1`

For an exhaustive list of dependencies, see the `environment.yml` file. 
