import streamlit as st
import pandas as pd
from predict import predict_transaction

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="AI Transaction Risk System",
    page_icon="💳",
    layout="wide"
)
# ====================================
# SIDEBAR
# ====================================

st.sidebar.image(
    "https://img.icons8.com/color/96/bank-card-back-side.png",
    width=80
)

st.sidebar.title("AI Risk System")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🔍 Transaction Prediction",
        "📊 Business Insights",
        "🤖 About Model"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("Model Status : Online 🟢")

st.sidebar.write("Algorithm")
st.sidebar.info("Random Forest")

st.sidebar.write("Threshold")
st.sidebar.info("0.05")

st.sidebar.write("Version")
st.sidebar.info("1.0")

# -------------------------
# Title
# -------------------------
if page == "🔍 Transaction Prediction":

    st.title("💳 AI Transaction Risk Prioritization System")

    st.write(
        """
        Predict whether a transaction is fraudulent using Machine Learning.
        """
    )
    st.markdown("## Live Risk Monitoring")
    k1,k2,k3,k4=st.columns(4)

    k1.metric(
        "Model",
        "Random Forest"
    )

    k2.metric(
        "ROC-AUC",
        "0.73"
    )

    k3.metric(
        "Threshold",
        "0.05"
    )

    k4.metric(
        "Status",
        "🟢 Online"
    )

    st.write(
    """
    This application predicts whether a financial transaction is risky
    using a trained Random Forest Machine Learning model.
    """
    )

    st.markdown("---")
    st.markdown("## Enter Transaction Information")
    col1, col2 = st.columns(2)
    with col1:

        st.subheader("Transaction Details")

        amount = st.number_input(
            "Transaction Amount",
            min_value=0.0,
            value=5000.0
        )

        hour = st.slider(
            "Transaction Hour",
            0,
            23,
            12
        )

        merchant = st.selectbox(
            "Merchant Category",
            [
                "Fashion",
                "Food",
                "Fuel",
                "Grocery",
                "Jewelry",
                "Pharmacy",
                "Travel"
            ]
        )

        payment = st.selectbox(
            "Payment Method",
            [
                "Debit Card",
                "Net Banking",
                "UPI",
                "Wallet"
            ]
        )

        device = st.selectbox(
            "Device Type",
            [
                "Android",
                "iPhone",
                "Windows",
                "Mac"
            ]
        )
        with col2:
            st.subheader("Risk Parameters")

            merchant_risk = st.slider(
                "Merchant Risk Score",
                0.0,
                1.0,
                0.20
            )

            prev_txn = st.slider(
                "Previous Transactions (24 Hours)",
                0,
                20,
                2
            )

            device_changed = st.checkbox(
                "Device Changed"
            )

            location_changed = st.checkbox(
                "Location Changed"
            )
    predict = st.button(
        "🔍 Predict Risk"
    )


    if predict:

        prediction, probability, risk, recommendation = predict_transaction(

            amount,
            hour,
            merchant,
            payment,
            device,
            merchant_risk,
            prev_txn,
            device_changed,
            location_changed
        )

        # =====================
        # Metrics
        # =====================

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Fraud Probability",
            f"{probability*100:.2f}%"
        )

        col1.progress(probability)

        col2.metric(
            "Risk Bucket",
            risk
        )

        col3.metric(
            "Recommendation",
            recommendation
        )

        # =====================
        # Risk Card
        # =====================

        if probability >= 0.20:

            st.error("🔴 HIGH RISK\n\nManual Review Required")

        elif probability >= 0.05:

            st.warning("🟡 MEDIUM RISK\n\nMonitor Transaction")

        else:

            st.success("🟢 LOW RISK\n\nAuto Clear")
        st.markdown("---")

        st.subheader("Why was this transaction flagged?")
        reasons=[]
        if amount>15000:
            reasons.append("💰 High Transaction Amount")

        if merchant_risk>0.8:
            reasons.append("🏪 High Risk Merchant")

        if prev_txn>10:
            reasons.append("⚡ High Transaction Velocity")

        if device_changed:
            reasons.append("📱 Device Changed")

        if location_changed:
            reasons.append("📍 Location Changed")

        if hour<6:
            reasons.append("🌙 Night Transaction")
        if len(reasons)==0:

            st.success(
                "No significant fraud indicators detected."
            )

        else:

            for reason in reasons:

                st.write(reason)
        st.markdown("---")

        st.subheader("Transaction Summary")
        summary = pd.DataFrame({

        "Feature":[

            "Amount",

            "Hour",

            "Merchant",

            "Payment",

            "Device",

            "Merchant Risk",

            "Previous Transactions"

        ],

        "Value":[

            amount,

            hour,

            merchant,

            payment,

            device,

            merchant_risk,

            prev_txn

        ]

    })
        st.table(summary)
        st.markdown("---")

        st.subheader("Prediction Confidence")
        confidence=max(probability,1-probability)
        st.metric(

        "Confidence",

        f"{confidence*100:.2f}%"

    )
        report = pd.DataFrame({

        "Fraud Probability":[probability],

        "Risk Bucket":[risk],

        "Recommendation":[recommendation]

    })
        csv = report.to_csv(index=False)
        st.download_button(

        label="📥 Download Prediction Report",

        data=csv,

        file_name="FraudPrediction.csv",

        mime="text/csv"

    )
        st.markdown("---")

        st.subheader("Model Output")

        st.write("Prediction Class :", prediction)

        st.write("Fraud Probability :", probability)
        st.markdown("---")

    st.caption(
    """
    Developed by Harsh Sharma

    AI Transaction Risk Prioritization System

    Machine Learning • Streamlit • Power BI
    """
    )
elif page == "📊 Business Insights":

    st.title("📊 Business Insights Dashboard")

    st.markdown("---")
    k1, k2, k3, k4 = st.columns(4)

    k1.metric(
        "Transactions",
        "10,000"
    )

    k2.metric(
        "Fraud Cases",
        "445"
    )

    k3.metric(
        "Fraud Rate",
        "4.45%"
    )

    k4.metric(
        "Model",
        "Random Forest"
    )
    df = pd.read_excel(r"C:\Users\Harsh\Transaction_Risk_Prioritization_System\data\Synthetic_Transaction_Risk_Dataset.xlsx")
    st.subheader("Fraud Distribution")

    fraud_counts = df["IsFraud"].value_counts()

    st.bar_chart(fraud_counts)

    st.subheader("Payment Method Distribution")

    payment = df["PaymentMethod"].value_counts()

    st.bar_chart(payment)
    st.subheader("Merchant Category")

    merchant = df["MerchantCategory"].value_counts()

    st.bar_chart(merchant)
    st.subheader("City Distribution")

    city = df["City"].value_counts()

    st.bar_chart(city)
    st.caption(
    """
    Developed by Harsh Sharma

    AI Transaction Risk Prioritization System

    Machine Learning • Streamlit • Power BI
    """
    )
elif page == "🤖 About Model":

    st.title("🤖 About Machine Learning Model")

    st.markdown("---")
    left, right = st.columns(2)
    with left:

        st.subheader("Model Information")

        st.write("Algorithm : Random Forest")

        st.write("Features : 53")

        st.write("Threshold : 0.05")

        st.write("ROC AUC : 0.73")

        st.write("F1 Score : 0.15")
    with right:

        st.subheader("Business Objective")

        st.write(
            """
            This application predicts fraudulent
            transactions and prioritizes
            them for manual review.

            The goal is to reduce operational
            workload while improving fraud
            detection.
            """
        )
    st.caption(
    """
    Developed by Harsh Sharma

    AI Transaction Risk Prioritization System

    Machine Learning • Streamlit • Power BI
    """
    )
    