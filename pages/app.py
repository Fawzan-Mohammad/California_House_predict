import pandas as pd
import matplotlib.pyplot as plt
import joblib
import streamlit as st

@st.cache_resource
def load_model():
    return joblib.load("RF_Model.pkl")    

model = load_model()


st.title("Welcome To The Calofornia House Prediction Model", anchor=False)

with st.sidebar:
    # st.selectbox("Choose a model", ["Random Forest", "Linear Regression", "Ridge"])
    st.markdown("## 🏠 House Predictor")
    st.caption("California House Prediction Model")
    st.divider()

    st.markdown("### ⚙️ Model Settings")
    st.caption("Adjust Your Model Here")
    st.divider()

    st.caption("© 2026 California House Prediction Model")

# CREATING INPUT FIELDS cl

col1, col2, col3 = st.columns(3)

with col1:
    Med_Inc = st.number_input("Median Income", value = 3.5)
    House_Age = st.number_input("House Age", value = 20)
    Ave_Rooms = st.number_input("Average Rooms", value = 5.0)
    Ave_Occup = st.number_input("Average Occupation", value = 3.0)


with col2:
    Ave_Bedrooms = st.number_input("Average Bedrooms", value = 1.0)
    Population = st.number_input("Population", value = 1000)
    latitude = st.number_input("Latitude", value = 34.0)
    longitude = st.number_input("Longitude", value= -118.0)



# CREATING A DATAFRAME FOR INPUTS

input_data = pd.DataFrame(
    {
        "MedInc": [Med_Inc],
        "HouseAge": [House_Age],
        "AveRooms": [Ave_Rooms],
        "AveBedrms": [Ave_Bedrooms],
        "Population": [Population],
        "AveOccup": [Ave_Occup],
        "Latitude": [latitude],
        "Longitude": [longitude]
    }
)

with col3:
    with st.container(key="right-column"):
        st.write("MAKE YOUR PREDICTION HERE!")
        if st.button("Predict"):
            prediction =model.predict(input_data)
            actual_value = prediction[0] * 100000
            st.caption("📌 Note that predictions are for for demonstrations only not as a means to make decsions.")
            st.success(f"Predicted House Value is: ${actual_value:,.2f}")


st.html(
    """
    <style>

    .st-key-right-column{
    background-color: #1C0113;
    border:none;
    border-radius: 12px;
    width: 100%;
    padding: 15px;
    margin-left: 10px;
    }

    </style>

    """
)
    




