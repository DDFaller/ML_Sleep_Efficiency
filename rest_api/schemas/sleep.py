from pydantic import BaseModel
from typing import List
from models.sleep import Sleep 

class SleepSchema(BaseModel):
  """ Define como um doutor é apresentado na base de dados
  O atributo gender aceita dois valores 1 para Male 0 para Female
  Smoke é simplesmente 1 para fuma ou 0 para não fuma
  """
  Age: str = "21"
  Sex: str = "1"
  Sleep_duration: str = "8"
  REM_sleep_percentage: str = "18"
  Deep_sleep_percentage: str = "40"
  Light_sleep_percentage: str = "32"
  Awakenings: str = "0"
  Alcohol_consumption: str = "1"
  Caffeine_consumption: str = "2"
  Exercise_frequency: str = "3"
  Smoking: str = "0"
  Bedhour: str = "23"
  Wakehour: str = "7"



class FindSleepSchema(BaseModel):
  """ Define como um doutor deve ser buscado na base de dados
  """
  crm: str = "0000"


def apresenta_sono(Sleep: Sleep):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "Age": Sleep.Age,
        "Gender": Sleep.sex,
        "Sleep_frequency": Sleep.Sleep_duration
    }

