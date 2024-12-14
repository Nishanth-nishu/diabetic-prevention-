# diabetic-prevention-

### Project Title: Glycemic Risk Assessment and Management Assistant

### Project Description

This project, **Glycemic Risk Assessment and Management Assistant**, is a diabetes risk prediction and management tool that uses a combination of machine learning for risk assessment and **Gemini** (a generative AI model) for personalized health recommendations. The project aims to provide individuals with real-time guidance on lifestyle and dietary habits based on their health data, empowering them to take proactive steps in managing or preventing diabetes. By leveraging predictive analytics and the generative capabilities of Gemini, this solution combines data-driven insights with context-specific advice, making it a comprehensive digital health assistant.

### Project Overview

Diabetes is a chronic condition that affects millions, and early intervention is crucial for preventing progression and complications. This project employs machine learning algorithms to assess diabetes risk based on user-provided health metrics. Depending on the results, the system leverages **Gemini** to generate customized dietary and lifestyle recommendations tailored to each individual’s specific health profile. The recommendations support both prevention for at-risk individuals and management advice for those diagnosed with diabetes.

### Technical Components

1. **Machine Learning Model**:
   - **Algorithm**: A **Gradient Boosting Classifier** model is used to predict diabetes risk, as it combines multiple weak classifiers to enhance prediction accuracy.
   - **Features**: The model takes in eight features crucial for diabetes prediction:
     - Pregnancies
     - Glucose level
     - Blood Pressure
     - Skin Thickness
     - Insulin level
     - BMI (Body Mass Index)
     - Diabetes Pedigree Function (genetic influence)
     - Age
   - **Data Processing**: The data is split into training and testing subsets to evaluate model performance. Metrics like precision, recall, and F1 score are calculated, providing insights into the model’s accuracy.

2. **Gemini-Powered Recommendations**:
   - **Generative Model**: Gemini is used to generate detailed, personalized health advice. Based on the model’s prediction, Gemini suggests preventive or management-oriented recommendations, covering areas such as diet, exercise, and lifestyle modifications.
   - **Scenarios**:
     - **No Diabetes (Prediction = 0)**: If no diabetes is detected but insulin, glucose, or BMI levels are elevated, the system flags these risks and provides preventive recommendations, such as dietary changes and exercise plans.
     - **Diabetes Detected (Prediction = 1)**: If diabetes is predicted, Gemini provides tailored advice on managing the condition, including balanced meal plans, exercise routines, and daily lifestyle practices to help control blood glucose levels.

### User Experience

The assistant is designed to be interactive and user-friendly. Users input their health data, which the model processes to predict diabetes risk. If elevated levels are detected in certain features, Gemini generates context-aware advice on dietary and lifestyle improvements. This interactive approach enhances user engagement and supports informed decision-making, with detailed recommendations for both diabetes prevention and management.

### Project Workflow

1. **Data Input**: Users enter their values for all required health features.
2. **Risk Prediction**: The model evaluates the risk level based on the input data.
3. **Advice Generation with Gemini**:
   - If the model identifies potential risks without diabetes, Gemini suggests preventive habits.
   - If diabetes is predicted, Gemini provides a structured plan for managing blood glucose.
4. **Feedback Output**: The system presents a comprehensive report on the user’s health status and recommended actions, fostering self-management and prevention.

**video explanation link**: https://youtube.com/shorts/yhzyv5_YrWM?si=q_gsPn6cySRkwnyC

In summary, this project combines the predictive power of machine learning with Gemini’s generative capabilities to provide personalized health guidance for diabetes prevention and management.
