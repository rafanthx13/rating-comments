# Text Minig: Avaliador de Comentário

Trabalho de IA: Utilizaçâo de Rede Neural LSTM para aprender a classificar comentários sobre produtos com interface web usando Angular JS.

DataSet: https://www.kaggle.com/olistbr/brazilian-ecommerce/home

### Instalar no Linux

1. (Dados) Descompate o zip na pasta `/dados` para poder usar o `.csv`

2. (Web) na pasta `lib` execute no terminal `npm i` para instalar as dependências web para a página.

3. Para usar é recomendável instlar um `virtualenv` para rodar o flask. Basta seguir os seguintes passos (usando pytohn 3):

4. Execute os seguintes comandos no terminal: Instalar o virtual env, executalo, instlar as dependencias do python para o projeto, configurar `FLASK_APP` e rodar o server localmente.

```
$ sudo apt install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install flask
(venv) $ pip install flask_cors
(venv) $ pip install torch==1.5.1+cpu torchvision==0.6.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
(venv) $ pip install pandas
(venv) $ export FLASK_APP=server_txt.py
(venv) $ flask run
```

+ Tem que aparecer: `* Running on http://127.0.0.1:5000/`  indicando que está funcionando.
+ Para sair do flask, de CTRL+C e 
+ para sair desse ambiente, `deactivate`

5. Em seguida abra o `index.hmtl` pelo navegador e execute.

**Links úteis para instalação do virtualenv**

+ http://flask.pocoo.org/docs/1.0/installation/#install-create-env
+ https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais
+ https://www.tutorialspoint.com/flask/flask_environment.htm
+ https://linuxize.com/post/how-to-install-flask-on-ubuntu-18-04/



pip install --upgrade pip
pip install -r requirements.txt

> # gera requirements
pip freeze > requirements.txt



PIPENV

## INSTALAR

Just use pip:

$ pip install pipenv
Or, if you’re using Ubuntu 17.10:

$ sudo apt install software-properties-common python-software-properties
$ sudo add-apt-repository ppa:pypa/ppa
$ sudo apt update
$ sudo apt install pipenv

## UPDATE ANYTIME

$ pip install --user --upgrade pipenv

## Usar

pipenv shell

Vai abrir o shell

## MELHOR SITE PARA ENTENDER PIPENV

https://stackoverflow.com/questions/46330327/how-are-pipfile-and-pipfile-lock-used





==========


[[source]]

url = "https://pypi.python.org/simple"
verify_ssl = true


[packages]

Flask = "*"

[requires]

python_version = "3.6"

