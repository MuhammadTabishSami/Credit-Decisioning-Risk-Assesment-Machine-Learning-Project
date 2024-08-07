import os
import sys
import dill

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        print(f'Object saved to {file_path}')

    except Exception as e:
        print(f"Error saving object to {file_path}: {e}")
        raise CustomException(e, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}  # Initialize report dictionary to store model scores

        for model_name, model in models.items():
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = accuracy_score(y_train, y_train_pred)
            test_model_score = accuracy_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            obj = dill.load(file_obj)
            print(f'Loaded object of type: {type(obj)} from {file_path}')
            return obj
    except Exception as e:
        raise CustomException(e,sys)