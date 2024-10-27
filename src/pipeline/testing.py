import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import pipeline
# Example usage
if __name__ == "__main__":
    try:
        # Initialize the prediction pipeline
        model_path = r'E:\PBA-14\src\pipeline\model.pkl'  # Path to the model
        prediction_pipeline = pipeline.Prediction.PredictionPipeline(model_path=model_path)

        # Define input data as a dictionary (example with 8 features)
        input_data = {
            'feature1': 10.5,
            'feature2': 3.2,
            'feature3': 5.7,
            'feature4': 5.7,
            'feature5': 5.7,
            'feature6': 5.7,
            'feature7': 5.7,
            'feature8': 5.7
        }

        # Call the predict method and print the result
        result = prediction_pipeline.predict(input_data)
        print(f"Prediction: {result}")

    except Exception as e:
        print(f"An error occurred: {e}")
