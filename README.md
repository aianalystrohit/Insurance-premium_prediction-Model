# Insurance-premium_prediction-Model

**Problem Statement:**
The goal of this project is to give people an estimate of how much they need based on
their individual health situation. After that, customers can work with any health
insurance carrier and its plans and perks while keeping the projected cost from our
study in mind. This can assist a person in concentrating on the health side of an
insurance policy rather han the ineffective part.

Dataset:
Dataset Link: - [https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction](url)

Approach
Executing machine learning tasks such as Data Exploration, Data Cleaning, Feature Engineering, Model Building, and Model Testing to construct a solution capable of predicting health insurance premiums for individuals.

**Here's how each step was carried out**:

Data Exploration: Investigated the dataset using libraries like pandas, numpy, matplotlib, plotly, and seaborn.

Exploratory Data Analysis: Generated various graphs to gain deeper insights into both dependent and independent variables.

Feature Engineering: Rescaled numerical features and encoded categorical ones.

Model Building: Started with dataset splitting, then proceeded to train different Machine Learning Algorithms, including:

Linear Regression
Support vector regression
Random Forest Regressor
Gradient Boosting Regressor
Model Selection: Evaluated all models based on their mean absolute error(mae) and R-squared metrics.

Pickle File: Chose the model with the best RMSE score and R-squared value, then generated a pickle file using the pickle library.

Webpage & Deployment: Designed a web application that collects user inputs and presents outputs. The project was subsequently deployed on the streamlit Platform.

Each of these steps was meticulously executed to create a comprehensive solution for predicting health insurance premiums, involving everything from initial data exploration to the final deployment of the predictive model on a web interface.

Web app interface
![Screenshot 2024-09-24 182904](https://github.com/user-attachments/assets/2ce8eff3-9674-4350-8132-1defb464a875)


Link for the web app -[https://insurancepremiumprediction-j2kcdoauplgk9jb4cmmhq6.streamlit.app/](url)

Libraries used:
1) Pandas
2) Numpy
3) Matplotlib, Seaborn, Plotly
4) Scikit-Learn
5) Streamlit
6) HTML
7) CSS

