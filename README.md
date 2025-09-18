# Heart Disease Prediction 🫀

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE) [![Streamlit](https://img.shields.io/badge/streamlit-app-orange?logo=streamlit)](https://streamlit.io/)  

Predict the risk of **heart disease** using patient medical data with machine learning, featuring an interactive **Streamlit** web app.

---

## 🗂 Dataset

- **Source:** Kaggle – [Heart Disease Dataset](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)  
- **Target:** `HeartDisease` (0 = No, 1 = Yes)  
- **Features:** Age, Sex, Chest Pain Type, Resting BP, Cholesterol, Fasting Blood Sugar, ECG, Max Heart Rate, Exercise Angina, Oldpeak, ST Slope, etc.

---

## 🔍 Features

- End-to-end ML pipeline: **EDA → Preprocessing → Model Training → Evaluation → Deployment**  
- Handles **missing values**, categorical encoding, and feature scaling  
- Trains multiple models: Logistic Regression, KNN, SVM, Random Forest, XGBoost  
- Model evaluation: Accuracy, ROC-AUC, Confusion Matrix, Cross-Validation  
- **Interactive Streamlit app** for real-time predictions  
- Feature importance and interpretability included  

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone <your-repo-link>
cd heart-disease-prediction

pip install -r requirements.txt


streamlit run app.py

heart-disease-prediction/
│
├── heart.csv                 # Dataset
├── HeartDisease.ipynb        # EDA & Model Training
├── app.py                    # Streamlit Deployment
├── heart_disease_model.pkl   # Saved Best Model
├── requirements.txt          # Dependencies
└── README.md                 # Project Documentation

