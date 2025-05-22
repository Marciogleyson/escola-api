from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"mensagem": "Olá Mundo"}

@app.get("/calculadora")
def calculadora(numero1: int, numero2: int):

    soma = numero1 + numero2
    return {"soma": soma}

@app.get("/processar-cliente")
def processar_dados_cliente(nome: str, idade: int, sobrenome: str):
    #nome_completo => snake_case
    # NomeCompleto => PascalCase
    # nomeCompleto => camelCase
    # nome-completo => kebad-case

    nome_completo = nome + " " + sobrenome
    ano_nascimento = datetime.now().year - idade   # from datetime import datetime

    if ano_nascimento >= 1990 and ano_nascimento < 2000:
        decada = " Decada de 90"
    elif ano_nascimento >= 1980 and ano_nascimento < 1990:
        decada = " Decada de 80"
    elif ano_nascimento >= 1970 and ano_nascimento < 1980:
        decada = " Decada de 70"
    else:
        decada = " Decada abaixo de 70 ou acima de 90"

    return {
        "nome_completo": nome_completo,
        "ano_nascimento": ano_nascimento,
        "decada": decada,
    }

