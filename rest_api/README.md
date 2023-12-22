

# ML_Sleep_Efficiency - API

Compartilhe seus estudos e aprenda com outras pessoas.

**ML_Sleep_Efficiency** tem como objetivo conectar e ajudar pessoas a estudarem através do compartilhamento de conteúdos gratuitos na internet de forma estruturada e didática entre usuários. Venha estudar com a comunidade **ML_Sleep_Efficiency** também!





# Clone o repositório

```
git clone https://github.com/DDFaller/ML_Sleep_Efficiency.git
```

Para executar a aplicação é necessário ter todas as libs (bibliotecas) python listadas no arquivo `requirements.txt` instaladas. 

#

### 2 - Criando um ambiente virtual (opcional)
s.

Você pode criar um  ambiente virtual a partir do seguinte comando:

```
python -m venv env
```

Após criar o ambiente virtual, você pode ativá-lo a partir do seguinte comando:

```
# Windows:
.\env\Scripts\activate.ps1

# Linux ou Mac:
source ./python_env/bin/activate
```

### 3 - Instalando as dependências


```
pip install -r requirements.txt
```
### 4 - Executando a API
Finalmente, para executar a API, basta executar o seguinte comando:

```
(env)$ flask run 
```

Em modo de desenvolvimento, é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte, conforme abaixo:

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

