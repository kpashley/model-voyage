import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the pre-trained Random Forest model
model = joblib.load("random_forest_model.pkl")

def predict_voyage_days(start_continent, start_med, kisan_trading_fze, industries_chimiques, wc):
    # Prepare input features
    input_data = {
        'Start_Continent': [start_continent],
        'Start_Med': [start_med],
        'KISAN INTERNATIONAL TRADING FZE': [kisan_trading_fze],
        'INDUSTRIES CHIMIQUES DUE SENEGAL': [industries_chimiques],
        'WC': [wc]
    }
    input_df = pd.DataFrame(input_data)
    
    # Make prediction
    prediction = model.predict(input_df)
    
    return prediction[0]

def main():
    st.title("Voyage Days Prediction (1 if Yes, 0 if No)")

    # Input fields
    start_continent = st.selectbox("Starting from Continent?:", ["1", "0"])
    start_med = st.selectbox("Starting from Mediterranean?:", ["1", "0"])
    kisan_trading_fze = st.selectbox("Charterer,Kisan?:", ["1", "0"])
    industries_chimiques = st.selectbox("Charterer, Industries Chimiques?:", ["1", "0"])
    wc = st.selectbox("WC:", ["1", "0"])

    # Calculate button
    if st.button("Predict Voyage Days"):
        # Make prediction
        prediction = predict_voyage_days(start_continent, start_med, kisan_trading_fze, industries_chimiques, wc)
        
        # Display prediction
        st.success(f"Predicted Voyage Days: {prediction}")

if __name__ == "__main__":
    main()
