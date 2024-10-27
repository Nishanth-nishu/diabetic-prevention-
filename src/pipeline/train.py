import os
import sys
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from src.logger import logging
from src.exception import CustomException

class TrainingPipeline:
    def __init__(self, data_path: str):
        self.data_path = data_path  # Use the parameter passed during initialization
    
    def load_data(self):
        try:
            # Load the dataset
            data = pd.read_csv(self.data_path)
            logging.info(f"Data loaded successfully from {self.data_path}")
            return data
        except Exception as e:
            logging.error("Failed to load data")
            raise CustomException(e, sys)
    
    def train_model(self, data: pd.DataFrame):
        try:
            # Separate features and target variable
            X = data.drop('Outcome', axis=1)
            y = data['Outcome']
            
            # Split the data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            logging.info(f"Data split into training and testing sets")
            
            # Initialize and train the SVM model
            model = SVC(C=1, kernel='linear')
            model.fit(X_train, y_train)
            logging.info(f"Model trained successfully")
            
            # Evaluate the model
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            logging.info(f"Model accuracy: {accuracy:.4f}")
            
            return model, accuracy
        except Exception as e:
            logging.error("Failed to train model")
            raise CustomException(e, sys)
    
    def save_model(self, model, model_path: str):
        try:
            # Save the trained model
            joblib.dump(model, model_path)
            logging.info(f"Model saved successfully at {model_path}")
        except Exception as e:
            logging.error("Failed to save model")
            raise CustomException(e, sys)


