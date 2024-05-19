# views.py

import os
from flask import Blueprint, render_template, request, session
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd

views = Blueprint('views', __name__)

# Specify absolute paths
base_path = 'E:\\Personal\\Machine Learning\\Intern pe\\Projects\\Diabetes Prediction\\website'
scaler_path = os.path.join(base_path, 'scaler.joblib')
classifier_path = os.path.join(base_path, 'classifier.joblib')
csv_path = 'E:\\Personal\\Machine Learning\\Intern pe\\Datasets\\diabetes.csv'  # Correct the CSV path

# Initialize scaler and classifier variables
scaler = None
classifier = None

# Load the dataset
diabetes_dataset = pd.read_csv(csv_path)

# Features (X) and target (Y)
X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']

scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)

X = standardized_data
Y = diabetes_dataset['Outcome']

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Initialize the classifier
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

@views.route('/')
def home():
    user_authenticated = session.get('user_authenticated', False)
    return render_template('home.html', user_authenticated=user_authenticated)

@views.route('/predict_diabetes', methods=['GET'])
def predict_diabetes_form():
    return render_template('predict_diabetes.html')

@views.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():
    global scaler, classifier  # Ensure we use the global variables

    # Get input data from the form
    pregnancies = float(request.form.get('pregnancies'))
    glucose = float(request.form.get('glucose'))
    blood_pressure = float(request.form.get('blood_pressure'))
    skin_thickness = float(request.form.get('skin_thickness'))
    insulin = float(request.form.get('insulin'))
    bmi = float(request.form.get('bmi'))
    diabetes_pedigree_function = float(request.form.get('diabetes_pedigree_function'))
    age = float(request.form.get('age'))

    # Reshape the input data
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

    # Standardize the input data
    standardized_data = scaler.transform(input_data)

    # Predict diabetes
    prediction = classifier.predict(standardized_data)

    # Print input data for debugging
    print("Input Data:", input_data)
    print("Prediction:", prediction)

    if prediction[0] == 1:
        result = 'The person is diabetic.'
    else:
        result = 'The person is not diabetic.'

    return render_template('prediction_result.html', result=result)
