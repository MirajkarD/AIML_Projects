 # Print input data for debugging
    print("Input Data:", input_data)

    # Predict diabetes
    prediction = classifier.predict(standardized_data)
    print("Prediction:", prediction)

    if prediction[0] == 0:
        result = 'The person is not diabetic.'
    else:
        result = 'The person is diabetic.'

    return render_template('prediction_result.html', result=result)
