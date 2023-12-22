from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, render_template,request
from urllib.parse import unquote
from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.exc import IntegrityError


from flask_cors import CORS
from logger import logger
from schemas import *
from models import *
import datetime

from use_cases import \
    add_sleep, \
    get_sleeps

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info,template_folder =".")
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
sleep_tag = Tag(name="Eficiência de sono", description="Avaliação e visualização dos hábitos de sono")



@app.get('/', tags = [home_tag])
def home():
    """Redireciona para /openapi, tela contendo a documentação.
    """
    return render_template("home.html"), 200


@app.post('/sleep', methods =['POST'],
           responses={"200": SleepSchema,"409": ErrorSchema, "400": ErrorSchema})
def login(form: SleepSchema):
    """Avalia um novo usuário a respeito da qualidade do sono

    Retorna o resultado da avaliação ["Pessimo","Ruim","Bom","Otimo"].
    """
    response = add_sleep(form)
    return response

@app.get('/sleep', tags=[sleep_tag], methods = ['GET'],
          responses={"200": SleepSchema,"409": ErrorSchema, "400": ErrorSchema})
def get_sono(form: SleepSchema):
    """Visualiza a avaliação
    """
    response = get_sleeps(form)
    return response



