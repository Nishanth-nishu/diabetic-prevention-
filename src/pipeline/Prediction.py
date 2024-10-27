import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import joblib
import numpy as np
from src.logger import logging
from src.exception import CustomException

class PredictionPipeline:
    def __init__(self, model_path: str):
        self.model_path = r'E:\PBA-14\src\pipeline\model.pkl'  # Using a raw string
        self.model = None
        try:
            self.model = joblib.load(self.model_path)
            logging.info(f"Model loaded successfully from {self.model_path}")
        except Exception as e:
            logging.error("Failed to load model")
            raise CustomException(e, sys)
    
    def predict(self, data: dict):
        try:
            # Convert input data into an array format for model prediction
            input_data = np.array(list(data.values())).reshape(1, -1)
            logging.info(f"Input data reshaped for prediction: {input_data}")
            
            prediction = self.model.predict(input_data)
            logging.info(f"Prediction made: {prediction}")
            return prediction
        except Exception as e:
            logging.error("Error in making prediction")
            raise CustomException(e, sys)


