"""
@author: Rohit Sharma
"""
import streamlit as st
import joblib
from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os, sys

logging.info((f"Making an app for insurance premium prediction"))

try:
    def main():
        # Set the page configuration
        st.set_page_config(
            page_title="Health Insurance Cost Prediction",
            page_icon="🏥",
            layout="centered",
            initial_sidebar_state="collapsed"
        )

        # Apply CSS styling for the background image and text color
        st.markdown(
            """
            <style>
            body {
                background-image: url("https://images.ctfassets.net/uwf0n1j71a7j/25NHaw7GRToxh2z3yZkJGV/0c402580b18b451c83f01242d36ab4dc/arogya-sanjeevani-policy.png");
                background-size: cover;
            }
            .stApp {
                background-color: rgba(288, 100, 100, 0.7);
                padding: 2rem;
                border-radius: 10px;
                width: 500px;
                max-width: 90%;
            }
            .stApp h2 {
                color: black;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Render the UI components inside a container div
        st.markdown('<div class="stApp">', unsafe_allow_html=True)

        # Render the application title
        st.markdown("<h2 style='text-align: center;'>Health Insurance Cost Prediction Using ML</h2>", unsafe_allow_html=True)

        # Load the ML model
        model = joblib.load("Eda_and_Model_building/GB_MODEL.joblib")

        # Input fields for user input
        p1 = st.number_input("Enter Your Age", min_value=18, max_value=100, value=25)
        
        s1 = st.selectbox('Sex', ('Male', 'Female'))
        p2 = 1 if s1 == 'Male' else 0
            
        p3 = st.number_input("Enter Your BMI Value", min_value=0.0, value=25.0)
        
        p4 = st.selectbox("Number of Children", (0, 1, 2, 3, 4), index=0)
        
        s2 = st.selectbox("Smoker", ("No", "Yes"))
        p5 = 1 if s2 == 'Yes' else 0
            
        region_mapping = {
            "1": "Southwest",
            "2": "Southeast",
            "3": "Northwest",
            "4": "Northeast"
        }
        p6 = st.selectbox("Region", ("1", "2", "3", "4"), index=0, format_func=lambda x: region_mapping[x])

        if st.button('Predict'):
            pred = model.predict([[p1, p2, p3, p4, p5, p6]])
            
            st.balloons()
            st.success('Your Insurance Cost is ${:.2f}'.format(pred[0]))
            
        # Close the container div
        st.markdown('</div>', unsafe_allow_html=True)
except Exception as e:
    raise InsuranceException(e, sys)

if __name__ == '__main__':
    main()
