import pickle
from models.ml_predictor import Predictor

predictor = Predictor('D:/Workspace/ML/rest_api/modelo_treinado.pkl')


saidas = predictor.preditor({'age': '21', 'gender': '1', 'sleep_hours': '8', 'wake_ups': '0', 'alcohol_consumption': '0', 'coffee_consumption': '0', 'exercise_frequency': '5', 'smoke': '0'})
print(saidas)