# 🛒 Customer Purchase Intention Prediction (Binary Classification)

## 📌 Overview
This project aims to predict whether an online shopper will make a purchase based on their browsing behavior.  
It is a **binary classification problem** where the output is either:
- 0 → No Purchase  
- 1 → Purchase  

---

## 🎯 Problem Statement
E-commerce platforms collect large amounts of user interaction data.  
The objective of this project is to build a machine learning model that can accurately predict **customer purchase intention** using session-based features.

---

## 📂 Dataset
- Each row represents a user session.
- Features include:
  - Administrative, Informational, Product-related pages
  - Bounce Rate, Exit Rate
  - Page Value
  - Traffic Type, Visitor Type
  - Month, Weekend
- Target Variable:
  - `Revenue` (0 = No Purchase, 1 = Purchase)

---

## ⚙️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 🔍 Approach

### Data Preprocessing
- Handled missing values
- Encoded categorical variables
- Applied feature scaling

### Exploratory Data Analysis (EDA)
- Analyzed feature distributions
- Correlation heatmaps
- Identified important features

### Model Building
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

### Model Evaluation
- Accuracy
- Precision
- Recall
- F1-score[ As the dataset have slight data imbalance]
- ROC-AUC Score

---

## 📊 Results
- Ensemble models performed better compared to baseline models
- Random Forest and Gradient Boosting achieved the best performance
