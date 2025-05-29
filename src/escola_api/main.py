from datetime import datetime, date
from typing import Optional

from fastapi import HTTPException
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)


@app.get("/")
def index():
    return {"mensagem": "Olá Mundo"}


@app.get("/calculadora")
def calculadora(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {"soma": soma}


@app.get("/processar-cliente")
def processar_dados_cliente(nome: str, idade: int, sobrenome: str):
    # nome_completo => snake_case
    # NomeCompleto => PascalCase
    # nomeCompleto => camelCase
    # nome-completo => kebad-case

    nome_completo = nome + " " + sobrenome
    ano_nascimento = datetime.now().year - idade  # from datetime import datetime

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


class Curso(BaseModel):
    id: int = Field()
    nome: str = Field()
    sigla: Optional[str] = Field(default=None)


class CursoCadastro(BaseModel):
    nome: str = Field()
    sigla: str = Field()


class CursoEditar(BaseModel):
    nome: str = Field()
    sigla: str = Field()


cursos = [
    # instanciado um objeto da classe Curso
    Curso(id=1, nome="Python Web", sigla="PY1"),
    Curso(id=2, nome="GitHub", sigla="GT")
]


# localhost:8000/docs
@app.get("/api/cursos")
def listar_todos_cursos():
    return cursos


@app.get("/api/cursos/{id}")
def obter_por_id_cursos(id: int):
    for curso in cursos:
        if curso.id == id:
            return curso
    # Lançando um exceção com o status code de 404(não encontrado)
    raise HTTPException(status_code=404, detail="Curso não encontrado co id: {id}")


# CRUDE


@app.post("/api/cursos")
def cadastrar_curso(form: CursoCadastro):
    ultimo_id = max([curso.id for curso in cursos], default=0)

    # instanciar um objeto da class Curso
    curso = Curso(id=ultimo_id + 1, nome=form.nome, sigla=form.sigla)

    cursos.append(curso)

    return curso


@app.delete("/api/cursos/{id}", status_code=204)
def apagar_curso(id: int):
    for curso in cursos:
        if curso.id == id:
            cursos.remove(curso)
            return
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@app.put("/api/cursos/{id}", status_code=200)
def editar_curso(id: int, form: CursoEditar):
    for curso in cursos:
        if curso.id == id:
            curso.nome = form.nome
            curso.sigla = form.sigla
            return curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


## Exercicio

class Aluno(BaseModel):
    id: int = Field()
    nome: str = Field()
    sobrenome: str = Field()
    cpf: str = Field()
    data_nascimento: datetime = Field(alias="dataNascimento")


alunos = [
    Aluno(id=1, nome="Marcio ", sobrenome="Ramos", cpf="123.456.789-00", dataNascimento=date(1990, 5, 7))
]


@app.get("/api/alunos", status_code=200)
def lista_todos_alunos():
    return alunos


class AlunoCadastro(BaseModel):
    nome: str = Field()
    sobrenome: str = Field()
    cpf: str = Field()
    data_nascimento: datetime = Field(alias="dataNascimento")


class AlunoEditar(BaseModel):
    nome: str = Field()
    sobrenome: str = Field()
    cpf: str = Field()
    data_nascimento: datetime = Field(alias="dataNascimento")



alunos = [
    Aluno(id=1, nome="Marcio", sobrenome="Ramos", cpf="123.456.789-00", dataNascimento=date(1990, 5, 25)),
    Aluno(id=2, nome="Kauã", sobrenome="Ramos", cpf="123.888.789-23", dataNascimento=date(1990, 5, 25)),
    Aluno(id=3, nome="Ana ", sobrenome="Ramos", cpf="047.456.740-33", dataNascimento=date(1990, 5, 25)),
]


@app.get("/api/alunos/{id}")
def listar_aluno_id(id: int):
    for aluno in alunos:
        if aluno.id == id:
            return aluno
    raise HTTPException(status_code=404, detail=f" Aluno não encontrado com id: {id}")


@app.post("/api/alunos")
def cadastrar_aluno(form: AlunoCadastro):
    ultimo_id = max([aluno.id for aluno in alunos], default=0)

    aluno = Aluno(id=ultimo_id + 1, nome=form.nome, sobrenome=form.sobrenome, cpf=form.cpf,
                  dataNascimento=form.data_nascimento)
    alunos.append(aluno)
    return aluno


@app.put("/api/alunos/{id}")
def editar_aluno(id: int, form: AlunoEditar):
    for aluno in alunos:
        if aluno.id == id:
            aluno.nome = form.nome
            aluno.sobrenome = form.sobrenome
            aluno.cpf = form.cpf

            aluno.data_nascimento = form.data_nascimento
            return aluno
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado")


@app.delete("/api/alunos/{id}")
def apagar_aluno(id: int):
    for aluno in alunos:
        if aluno.id == id:
            alunos.remove(aluno)
            return
    raise HTTPException(status_code=404, detail=f"Aluno com o id não encontrado")


if __name__ == "__main__":
    uvicorn.run("main:app")
