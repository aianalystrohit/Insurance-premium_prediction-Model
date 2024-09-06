# Insurance Premium Prediction
### Problem Statement :
The primary objective of this initiative is to offer individuals an insight into the potential financial requirements for their health coverage, tailored to their specific health circumstances. Armed with this understanding, individuals can then navigate through the offerings of different health insurance providers, taking into consideration the projected expenses from our assessment. This approach empowers individuals to focus their attention on the essential health-related aspects of an insurance plan, while sidestepping any convoluted or unnecessary complexities.

### Dataset:
The dataset has been sourced from a Kaggle repository, and you have the option to download it from there: [download the dataset](https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction)

### Approach
Executing machine learning tasks such as Data Exploration, Data Cleaning, Feature Engineering, Model Building, and Model Testing to construct a solution capable of predicting health insurance premiums for individuals.

Here's how each step was carried out:

**Data Exploration:** Investigated the dataset using libraries like pandas, numpy, matplotlib, plotly, and seaborn.

**Exploratory Data Analysis:** Generated various graphs to gain deeper insights into both dependent and independent variables.

**Feature Engineering:** Rescaled numerical features and encoded categorical ones.

**Model Building:** Started with dataset splitting, then proceeded to train different Machine Learning Algorithms, including:
- Linear Regression
- Support vector regression
- Random Forest Regressor
- Gradient Boosting Regressor

**Model Selection:** Evaluated all models based on their mean absolute error(mae) and R-squared metrics.

**Pickle File:** Chose the model with the best RMSE score and R-squared value, then generated a pickle file using the pickle library.

**Webpage & Deployment:** Designed a web application that collects user inputs and presents outputs. The project was subsequently deployed on the streamlit  Platform.

Each of these steps was meticulously executed to create a comprehensive solution for predicting health insurance premiums, involving everything from initial data exploration to the final deployment of the predictive model on a web interface.

### Web app interface 
![alt text](https://github.com/Shekharmeena28/Insurance_premium_prediction/blob/main/Image/Screenshot%202023-06-23%20182904.png)

Link for the web app
https://insurancepremiumprediction-j2kcdoauplgk9jb4cmmhq6.streamlit.app/
### Libraries used:
    1) Pandas
    2) Numpy
    3) Matplotlib, Seaborn, Plotly
    4) Scikit-Learn
    5) Streamlit
    6) HTML
    7) CSS

**Documentation**
HIGH LEVEL DESIGN: [https://drive.google.com/file/d/1Y9MCtNy6X27uLZPwhjfy7pbGEQD1lc3b/view?usp=drive_link](url)

LOW LEVEL DESIGN:[https://drive.google.com/file/d/1qucHMJ_4sXWQfbd1VgGOh6SDV8MEiLJw/view?usp=drive_link](url)


ARCHITECTURE: [https://drive.google.com/file/d/1mrYVzAl5-AcWjW6vN4G_ma3O-vKgTjnK/view?usp=drive_link](url)

WIREFRAME DOCUMENT: [https://drive.google.com/file/d/1CnSpB7IPRfwbUo0bB1q5tLN6vkMK7_Dt/view?usp=drive_link](url)

DETAIL PROJECT REPORT: [https://drive.google.com/file/d/114K9JhJLalD3sPNMp87AadAC04qQY8OW/view?usp=drive_link](url)

Project demo video:

