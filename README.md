# 💳 AI Transaction Risk Prioritization System

An end-to-end Machine Learning application that predicts high-risk financial transactions and prioritizes them for manual review using behavioral analytics and fraud detection techniques.

---

## 📌 Project Overview

Financial institutions process millions of transactions every day, making it impossible to manually review every suspicious transaction.

This project simulates a real-world transaction risk operations framework used by banks and payment networks to:

- Detect potentially fraudulent transactions
- Assign a fraud probability score
- Categorize transactions into risk buckets
- Recommend operational actions (Auto Clear, Monitor, Manual Review)
- Reduce manual investigation workload through intelligent prioritization

The solution includes data preprocessing, feature engineering, machine learning, an interactive Streamlit web application, and a business intelligence dashboard.

---

## 🚀 Live Features

- ✅ Fraud Probability Prediction
- ✅ Risk Bucket Classification
- ✅ Manual Review Recommendation
- ✅ Interactive Streamlit Web Application
- ✅ Business Insights Dashboard
- ✅ Download Prediction Report
- ✅ Merchant Risk Analysis

---

## 🛠 Tech Stack

### Programming
- Python

### Machine Learning
- Scikit-learn
- Random Forest
- Logistic Regression
- XGBoost
- Decision Tree

### Data Processing
- Pandas
- NumPy

### Visualization
- Power BI
- Matplotlib
- Plotly
- Streamlit

### Model Deployment
- Streamlit Community Cloud

### Version Control
- Git
- GitHub

---

# 📂 Project Structure

```text
Transaction_Risk_Prioritization_System

│
├── data/
│     Synthetic_Transaction_Risk_Dataset.xlsx
│
├── models/
│     fraud_model.pkl
│     feature_columns.pkl
│
├── notebook/
│     Fraud_Detection.ipynb
│
├── streamlit/
│     app.py
│     predict.py
│
├── dashboard/
│     Fraud_Dashboard.pbix
│
├── requirements.txt
│
└── README.md
```

---

# 📊 Dataset

The dataset simulates real-world payment transaction data and contains customer, merchant, behavioral, and transaction attributes.

### Key Features

- Transaction Amount
- Merchant Category
- Merchant Risk Score
- Payment Method
- Device Type
- Transaction Hour
- Previous Transactions (24H)
- Device Change
- Location Change
- Customer Account Age
- Fraud Label

---

# ⚙ Feature Engineering

The project includes extensive feature engineering to improve fraud detection performance.

Engineered Features include:

- Amount Ratio
- Amount Deviation
- Absolute Deviation
- High Value Transaction
- High Risk Merchant
- Night Transaction
- Transaction Velocity
- Composite Risk Score
- New Customer Indicator
- Old Customer Indicator

---

# 🤖 Machine Learning Pipeline

The project follows an end-to-end ML workflow:

1. Data Cleaning
2. Exploratory Data Analysis
3. Feature Engineering
4. One-Hot Encoding
5. Train-Test Split
6. Model Training
7. Hyperparameter Tuning
8. Model Evaluation
9. Threshold Optimization
10. Model Deployment

---

# 📈 Models Evaluated

- Logistic Regression
- Decision Tree
- Random Forest ⭐
- XGBoost

Random Forest was selected as the final model based on overall predictive performance and robustness.

---

# 📊 Evaluation Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- Classification Report

Threshold tuning was performed to optimize fraud detection recall while maintaining operational efficiency.

---

# 🖥 Streamlit Application

The web application allows users to:

- Enter transaction details
- Predict fraud probability
- View risk bucket
- Receive operational recommendations
- Download prediction reports
- Explore business insights

---

# 📊 Business Dashboard

The Power BI dashboard includes:

- Fraud Distribution
- Merchant Category Analysis
- Payment Method Analysis
- City-wise Transactions
- Fraud Trends
- High-Risk Merchant Identification
- KPI Cards
- Risk Monitoring Dashboard

---

# 💼 Business Impact

The proposed framework enables organizations to:

- Prioritize high-risk transactions
- Reduce manual review effort
- Improve fraud detection efficiency
- Support risk operations teams
- Enable scalable transaction monitoring

---

# 📷 Screenshots

## Streamlit Application

(Add screenshot here)

---

## Power BI Dashboard

(Add screenshot here)

---

# 🔮 Future Enhancements

- SHAP Explainability
- Real-time Prediction API
- Batch Transaction Scoring
- Cloud Deployment
- Authentication & User Login
- Database Integration
- Live Fraud Monitoring Dashboard

---

# ▶ How to Run Locally

### Clone Repository

```bash
git clone https://github.com/yourusername/Transaction_Risk_Prioritization_System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
cd streamlit

python -m streamlit run app.py
```

---

# 📚 Skills Demonstrated

- Machine Learning
- Feature Engineering
- Fraud Analytics
- Classification Modeling
- Threshold Optimization
- Business Intelligence
- Data Visualization
- Streamlit Deployment
- Power BI
- Python
- Model Deployment
- Git & GitHub

---

# 👨‍💻 Author

**Harsh Sharma**

B.Tech Mechanical Engineering  
National Institute of Technology (NIT) Jamshedpur

Interested in:

- Data Science
- Business Analytics
- Machine Learning
- Fraud Analytics
- Financial Risk Analytics


---

⭐ If you found this project useful, consider giving the repository a star.
