from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from  models import Base
from dataclasses import dataclass
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
@dataclass
class Predictor():
    path: str
    
    def __init__(self, model_path):        
      self.path = model_path 
      pickle_in = open(model_path,'rb')
      self.model_pickle = pickle.load(pickle_in)
      pickle_in.close()

    def predict(self, parameters_list):
      atributos = ['Age', 
                   'Sleep duration',
                   'REM sleep percentage',
                   'Deep sleep percentage',
                   'Light sleep percentage',
                   'Awakenings',
                   'Caffeine consumption',
                   'Alcohol consumption',
                   'Exercise frequency',
                   'sex',
                   'smoking',
                   'Bedhour',
                   'Wakehour']
      entrada = pd.DataFrame(parameters_list,columns = atributos, index= [0])
      array_entrada = entrada.values
      X_entrada = array_entrada[:,0:12].astype(float)
      print(X_entrada)
      scaler = StandardScaler()
      # Padronização nos dados de entrada usando o scaler utilizado em X
      rescaledEntradaX = scaler.fit(X_entrada)

      print(rescaledEntradaX)
      saidas = self.model_pickle.predict(rescaledEntradaX)
      return saidas
    
    def preditor(self,parameters_list):
       X_input = np.array([parameters_list['Age'], 
                   parameters_list['Sleep duration'],
                   parameters_list['REM sleep percentage'],
                   parameters_list['Deep sleep percentage'],
                   parameters_list['Light sleep percentage'],
                   parameters_list['Awakenings'],
                   parameters_list['Caffeine consumption'],
                   parameters_list['Alcohol consumption'],
                   parameters_list['Exercise frequency'],
                   parameters_list['sex'],
                   parameters_list['smoking'],
                   parameters_list['Bedhour'],
                   parameters_list['Wakehour']])
       X_input = X_input.astype(float)
       return self.model_pickle.predict(X_input.reshape(1,-1))
    