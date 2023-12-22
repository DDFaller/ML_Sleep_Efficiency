from sqlalchemy.exc import IntegrityError
from models.sleep import Sleep
from logger import logger
import pickle
from sklearn.preprocessing import StandardScaler
from models.ml_predictor import Predictor

def add_sleep(form):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    sleep = Sleep(
        Age = form.Age,
        Sleep_duration = form.Sleep_duration,
        REM_sleep_percentage = form.REM_sleep_percentage,
        Deep_sleep_percentage = form.Deep_sleep_percentage,
        Light_sleep_percentage = form.Light_sleep_percentage,
        Awakenings = form.Awakenings,
        Caffeine_consumption = form.Caffeine_consumption,
        Alcohol_consumption = form.Alcohol_consumption,
        Exercise_frequency = form.Exercise_frequency,
        sex = form.Sex,
        smoking = form.Smoking,
        Bedhour = form.Bedhour,
        Wakehour = form.Wakehour
        )
    print(sleep)
    try:
        print(sleep.to_dict())
        predictor = Predictor('D:/Workspace/ML/rest_api/modelo_treinado.pkl')
        saidas = predictor.preditor(sleep.to_dict())

        # efetivando o camando de adição de novo item na tabela
        return  {"message": saidas[0]}, 200
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome e marca já salvo na base :/"
        logger.warning(f"Erro ao adicionar produto '{sleep.Age}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        print(e)
        logger.warning(f"Erro ao adicionar produto '{sleep.Age}', {error_msg}")
        return {"mesage": error_msg}, 400