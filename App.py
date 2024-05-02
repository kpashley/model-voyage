import streamlit as st
import random

def calculate(start_region, end_region, charterer, cargo_qty, voyage_start_date):
    # Generate random values for TCE, Voyage Days, and Ballast Days
    tce = random.randint(10000, 15000)
    voyage_days = random.randint(25, 55)
    ballast_days = random.randint(5, 10)
    
    # Perform some calculation based on start and end regions, character, and cargo quantity
    result = {
        "Start Region": start_region,
        "End Region": end_region,
        "Charterer": charterer,
        "Quantity of Cargo": cargo_qty,
        "Voyage Days": voyage_days,
        "TCE": tce,
        "Ballast Days": ballast_days,
        "Voyage Start Date": voyage_start_date
    }
    return result

def main():
    st.title("Model Voyage Card Builder")

    # Categorical options for start region
    start_region_options = ["Continent", "Mediterranean", "Africa"]
    start_region = st.selectbox("Select Start Region:", start_region_options)

    # Categorical options for end region
    end_region_options = ["East Coast", "West Coast"]
    end_region = st.selectbox("Select End Region:", end_region_options)

    # Categorical options for charterer
    charterer_options = ["Kisan International", "Industries Chimiques"]
    charterer = st.selectbox("Select Charterer:", charterer_options)

    # Numeric input for quantity of cargo
    cargo_qty = st.number_input("Enter Quantity of Cargo:", min_value=10000)

    # Date input for voyage start date
    voyage_start_date = st.date_input("Select Voyage Start Date:")

    # Button to trigger calculation
    if st.button("Give me Model Voyage Card details"):
        # Perform calculation
        result = calculate(start_region, end_region, charterer, cargo_qty, voyage_start_date)

        # Display result in columns
        st.subheader("Model Voyage Card Details")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Start Region:", result["Start Region"])
            st.write("End Region:", result["End Region"])
            st.write("Charterer:", result["Charterer"])
            st.write("Voyage Start Date:", result["Voyage Start Date"])
        with col2:
            st.write("Quantity of Cargo:", result["Quantity of Cargo"])
            st.write("Voyage Days:", result["Voyage Days"])
            st.write("TCE:", result["TCE"])
            st.write("Ballast Days:", result["Ballast Days"])

        # Additional text in the output
        st.subheader("Smart Suggestion")
        st.write("Based on selected Voyage Start Date and Cargo Qty, here are the ships which are available with above details:")
        
        # Display cards side by side
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Stolt Maple")
            st.write("- TCE: 10200")
            st.write("- Ballast Days: 5")
            st.write("- Voyage Days: 35")
            st.write("- Arrival Date: 25-05-2024")
        
        with col4:
            st.subheader("Stolt Palm")
            st.write("- TCE: 11200")
            st.write("- Ballast Days: 3")
            st.write("- Voyage Days: 31")
            st.write("- Arrival Date: 22-05-2024")

if __name__ == "__main__":
    main()
