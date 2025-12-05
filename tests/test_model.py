import pytest
import pickle
import os
from app import app
import numpy as np

with open("model/iris_model.pkl",'rb') as f:
    model = pickle.load(f)

def test_model_predictions():
    input_data = [5.5,3.6,4.5,1.8]
    preds = model.predict([input_data])
    assert preds is not None
    assert isinstance(preds[0], (int, np.integer))

def test_flask_predict():
    with app.test_client() as client:
        form_data = {
            'sepal_length':5.5,
            'sepal_width':3.6,
            'petal_length':4.5,
            'petal_width':1.8
        }
        response = client.post("/predict",data = form_data)
        assert response.status_code==200
        assert 'Predicted Iris class:' in response.get_data(as_text=True)



