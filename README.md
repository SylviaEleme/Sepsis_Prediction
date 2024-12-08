# Sepsis-Classification-ML-Project-with-FAST-API-Integration
This repository houses a machine learning project focused on the early detection and classification of sepsis, and integrating the model into a web application using FAST API.

![image](https://github.com/user-attachments/assets/8fe0f43c-1a60-4b1f-9f18-d73ff39ec2b0)


This project aims to provide a streamlined tool for healthcare professionals to predict sepsis cases quickly and effectively.

# Project Overview:
**i. Data Collection and Preprocessing:** I loaded and preprocessed a comprehensive dataset containing clinical and physiological data from patients to train and evaluate the sepsis classification model.

**ii. Machine Learning Model:** I implemented a machine learning model tailored for sepsis classification. This model has been fine-tuned to achieve high accuracy in detecting sepsis early, which is crucial for timely intervention.

**iii. FAST API Integration:** I've seamlessly integrated the trained machine learning model into an API using FAST API. The API allows healthcare professionals to input patient data and receive instant predictions regarding sepsis risk.

**iv. Docker Containerization:** I deployed the application to Docker

## FastAPI Interface
After clicking on the link to the working FastAPI, click on "Try It Out", add the patient's medical details, and click on the **"EXECUTE"** button.
![image](https://github.com/user-attachments/assets/1aaa6704-f504-4d78-8376-ca1501a8ca6c)

### Before Prediction
![image](https://github.com/user-attachments/assets/81e7c1aa-4f0c-4c53-8f5b-8f5c08f8ee43)

### After Prediction
![image](https://github.com/user-attachments/assets/7a934ea8-c7e2-424d-9d75-dc7b15a95973)


# Project Setup:
To set up the project environment, follow these steps:

i. Clone the repository:

git clone my_github 

```bash 
https://github.com/Ojuolloh/Sepsis-Prediction-Using-FastAPI).git
```

ii. Create a virtual environment and install the required dependencies:

- **Windows:**
  ```bash
  python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt
  ```
You can copy each command above and run them in your terminal to easily set up the project environment.

## Project Structure
Start by setting up a directory structure for the project. Here’s the structure I used:
```bash
├── Sepsis-Classification-ML-Project-with-FastAPI-Deployment (Project's Root Directory)

    ├── venv (your virtual environment)
    
    ├── data (folder containing your datasets)
    
    ├── Sepsis_ML_Prediction_Deployment_With_FastAPI.ipynb (Jupyter Notebook containing your code and analysis)
    
    ├── model_and_key_components.pkl (your saved ML model and key components)
    
    ├── src
    
        ├── FastAPI
        
            ├── main.py (your FastAPI)
        
            ├── app.py (your swagger API)
            
    ├── Dockerfile (Your Dockerfile for containerizing the FastAPI with Docker)
    
    ├── .gitignore
    
    └── requirements.txt
```

## Business Understanding:

I began by understanding the problem domain, which involved predicting sepsis in ICU patients.
I defined the project goals and objectives, such as early sepsis detection, which can save lives.

## Data Understanding:
I collected the test and train datasets from Kaggle, which included various patient attributes. The train dataset had, sepsis, the target variable, while the test dataset did not have the target variable since this dataset is what I later used to predict sepsis. 

After an overview of the first few columns, I formulated the hypothesis and key Business questions that would guide the understanding of the datasets.

**Business Questions:** 

1.What are the key factors influencing the health outcomes in the patient data?
2.Can we predict certain health conditions based on the available features?
3.How do patient demographics and behaviors vary across different groups?
4.What correlations or patterns exist in the patient dataset?
5.How can the data be used to improve healthcare services or policies?


### Understanding the datasets
I conducted an in-depth exploration of the datasets to gain insights into the available variables, their distributions, and relationships, including:

- i. Column Information of The Datasets using the .info method.

- ii. Shape of The Datasets

- iii. Summary Statistics Datasets

- iv. Checking for Missing Values in The Datasets

- v. Checking for Duplicates in The Datasets

These steps provided an initial undertanding of the datasets to identify any data quality issues that informed the cleaning and pre-processing steps.

I then conducted an extensive Exploratory Data Analysis (EDA) to get insights into the structure and quality of the dataset.

### Exploratory Data Analysis (EDA)
During the EDA phase, a comprehensive investigation of the sepsis dataset was conducted to gain insights through various types of analyses.

i. **Univariate analysis:** I performed a thorough individual examination of each variable looking at aspects such as summary statistics (mean, median, standard deviation, and quartiles) using the .describe method to understand the central tendency and spread of the data.

ii. **Bivariate analysis:** Relationships between pairs of variables were explored to identify patterns and potential predictor variables for sepsis classification.

iii. **Multivariate analysis:** Relationships among multiple variables were examined simultaneously, allowing for a deeper understanding of their interactions and impact on sepsis.

In addition to these exploratory analyses, I tested my hypothesis and answered key analytical questions.

## Data Preparation:
- I preprocessed the data by performing data cleaning by:

 i. imputing zero values that did not make sense in some of the columns with the mean value of each age group.
 ii. Dropping unnecessary columns 

- I encoded the target variable (Sepsis), the only categorical variable needed for modeling, using Label Encoding.
- I then conducted feature engineering to select relevant features and prepare them for modeling.

## Evaluation:

I evaluated the model's performance on the testing dataset to ensure its generalizability.
I used various evaluation metrics to assess how well the model predicted sepsis cases.


## Deployment:
**i. FastAPI**. 
The model is deployed as a FastAPI web service, which provides an API for sepsis prediction. This deployment offers an intuitive interface for users to input patient data and obtain predictions.

**ii. Docker Containerization**
The application is containerized using Docker, making it easy to package and run in various environments with consistent behavior.


# Conclusion
Following the CRISP-DM methodology, I systematically addressed the sepsis prediction problem, from understanding the business context to deploying a machine learning model as a practical tool for early sepsis detection in clinical settings.

# Author

`Frankline Sande`

`Data Analyst`
