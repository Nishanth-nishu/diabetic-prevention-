from flask import Flask, render_template, request, jsonify
import pickle
from src.logger import logging
import numpy as np
import google.generativeai as genai

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model
model_path = "E:\PBA-14\src\pipeline\model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Configure the Gemini API with your API key
genai.configure(api_key='AIzaSyBMh7bQCD1tf_9w7C04zNoJocEtHg9KLjI')  # Replace with your actual API key

# Home page to show the input form
@app.route('/')
def home():
    return render_template('home.html')

# Route to handle form submission and prediction

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from form fields
        input_data = [float(request.form.get(key)) for key in ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
        input_array = np.array(input_data).reshape(1, -1)
        
        # Make prediction using the model
        prediction = model.predict(input_array)[0]
        
        # Add logging for prediction
        logging.info(f"Prediction made: {prediction} for input: {input_data}")

        # Logic for generating suggestions
        suggestions = ""
        if prediction == 1:  # If predicted diabetic
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content("Suggest a diabetic meal plan and lifestyle changes to manage blood sugar levels for someone with diabetes.")
            suggestions = response.text
            result = "The person is likely diabetic."
        else:  # If not diabetic
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content("Suggest healthy food habits and lifestyle changes to prevent diabetes for someone with high insulin, glucose, or BMI.")
            suggestions = response.text
            result = "The person is not diabetic."

        return render_template('home.html', result=result, suggestions=suggestions)

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'error': str(e)})


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
