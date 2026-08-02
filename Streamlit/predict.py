
import pandas as pd
import joblib
import os

# ============================
# LOAD MODEL AND FEATURE LIST
# ============================

# __file__ gives the location of predict.py
CURRENT_DIR = os.path.dirname(__file__)

# Move one folder up (Project Folder)
BASE_DIR = os.path.dirname(CURRENT_DIR)

# Path of model
MODEL_PATH = os.path.join(BASE_DIR, "models", "fraud_model.pkl")

# Path of feature columns
FEATURE_PATH = os.path.join(BASE_DIR, "models", "feature_columns.pkl")

# Load trained Random Forest model
model = joblib.load(MODEL_PATH)

# Load training column names
feature_columns = joblib.load(FEATURE_PATH)


# ============================
# PREDICTION FUNCTION
# ============================

def predict_transaction(
    amount,
    hour,
    merchant,
    payment,
    device,
    merchant_risk,
    prev_txn,
    device_changed,
    location_changed
):

    # ============================
    # CREATE EMPTY DATAFRAME
    # ============================

    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=feature_columns
    )

    # ============================
    # NUMERIC FEATURES
    # ============================

    input_df["Amount"] = amount

    input_df["TransactionHour"] = hour

    input_df["PrevTxn24H"] = prev_txn

    input_df["MerchantRiskScore"] = merchant_risk

    input_df["IsWeekend"] = 0

    input_df["AccountAgeDays"] = 365

    input_df["AvgCustomerAmount"] = 2500

    # ============================
    # DERIVED FEATURES
    # ============================

    amount_deviation = (amount - 2500) / 2500

    input_df["AmountDeviation"] = amount_deviation

    input_df["AmountRatio"] = amount / 2500

    input_df["AbsoluteDeviation"] = abs(amount_deviation)

    input_df["CompositeRiskScore"] = (
        merchant_risk +
        input_df["AmountRatio"].iloc[0] +
        prev_txn / 20
    ) / 3

    # ============================
    # BOOLEAN FEATURES
    # ============================

    input_df["DeviceChanged"] = int(device_changed)

    input_df["LocationChanged"] = int(location_changed)

    input_df["IsNightTransaction"] = int(hour < 6)

    input_df["HighValueTxn"] = int(amount > 15000)

    input_df["HighRiskMerchant"] = int(merchant_risk > 0.80)

    input_df["NewCustomer"] = 0

    input_df["OldCustomer"] = 1

    input_df["Month"] = 6

    # ============================
    # ONE HOT ENCODING
    # ============================

    merchant_col = f"MerchantCategory_{merchant}"

    if merchant_col in input_df.columns:
        input_df[merchant_col] = 1

    payment_col = f"PaymentMethod_{payment}"

    if payment_col in input_df.columns:
        input_df[payment_col] = 1

    device_col = f"DeviceType_{device}"

    if device_col in input_df.columns:
        input_df[device_col] = 1

    # ============================
    # MODEL PREDICTION
    # ============================

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    # ============================
    # RISK BUCKET
    # ============================

    if probability >= 0.20:

        risk = "🔴 High Risk"

        recommendation = "Manual Review"

    elif probability >= 0.05:

        risk = "🟡 Medium Risk"

        recommendation = "Monitor Transaction"

    else:

        risk = "🟢 Low Risk"

        recommendation = "Auto Clear"

    # ============================
    # RETURN RESULTS
    # ============================

    return (
        prediction,
        probability,
        risk,
        recommendation
    )
