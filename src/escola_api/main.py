from dataclasses import dataclass, field
from datetime import datetime
from fastapi import HTTPException
import uvicorn
from fastapi import FastAPI
from pygments.lexer import default
from dataclasses import dataclass, field

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

@dataclass
class Curso:
    id: int = field()
    nome: str = field()
    sigla: str = field()

@dataclass
class CursoCadastro:
    nome: str = field()
    sigla: str = field()

@dataclass
class CursoEditar:
    nome: str = field()
    sigla: str = field()


cursos = [
    #instanciado um objeto da classe Curso
    Curso(id = 1, nome = "Python Web", sigla = "PY1"),
    Curso(id = 2, nome = "GitHub", sigla = "GT")
]

#localhost:8000/docs
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
    ultimo_id = max([curso.id for curso in cursos], default = 0)

    # instanciar um objeto da class Curso
    curso = Curso(id = ultimo_id + 1, nome = form.nome, sigla= form.sigla)

    cursos.append(curso)

    return  curso

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

@dataclass
class Aluno:
    id: int = field()
    nome: str = field()
    sobrenome: str = field()
    cpf: str = field()
    data_nascimento: str = field()

alunos = [
    Aluno(id = 1, nome = "Marcio ", sobrenome = "Ramos", cpf = "123.456.789-00", data_nascimento = "14/04/1980")
]


@app.get("/api/aluno", status_code= 200 )
def lista_todos_alunos():
    return alunos


@dataclass
class AlunoCadastro:
    nome: str = field()
    sobrenome: str = field()
    cpf: str = field()
    data_nascimento: str = field()

alunos = [
    Aluno(id=1, nome="Marcio ", sobrenome="Ramos", cpf="123.456.789-00", data_nascimento="14/04/1980")
]

@app.get("/api/aluno/{id}")
def listar_aluno_id(id: int):
    for aluno in alunos:
        if aluno.id == id:
          return aluno
    raise HTTPException(status_code=404, detail=f" Aluno não encontrado com id: {id}")




if __name__ == "__main__":
    uvicorn.run("main:app")