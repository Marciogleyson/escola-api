from escola_api.schemas.aluno_schemas import AlunoCadastro, Aluno, AlunoEditar
from escola_api.app import router
from datetime import date
from fastapi import HTTPException

alunos = [
    # instanciando um objeto da Class Aluno
    Aluno(id=1, nome="João", sobrenome="Diniz", cpf="062.950.959-55", dataNascimento=date(1990, 5, 25)),
    Aluno(id=2, nome="Jaime", sobrenome="Jacób", cpf="066.950.959-55", dataNascimento=date(1990, 5, 25)),
    Aluno(id=3, nome="Mery", sobrenome="Mengarda", cpf="002.850.959-55", dataNascimento=date(1990, 5, 25))
]

@router.get("/api/alunos")
def listar_todos_alunos():
    return alunos

@router.get("/api/alunos/{id}")
def obter_por_id_alunos(id: int):
    for aluno in alunos:
        if aluno.id == id:
            return aluno

    # Lançando uma exceção com o status code de 404(não encontrado)
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")

@router.post("/api/alunos")
def cadastrar_aluno(form: AlunoCadastro):
    ultimo_id = max([aluno.id for aluno in alunos], default=0)

    # instanciar um objeto da classe Aluno
    aluno = Aluno(
        id=ultimo_id + 1,
        nome=form.nome,
        sobrenome=form.sobrenome,
        cpf=form.cpf,
        dataNascimento=form.data_nascimento
    )
    alunos.append(aluno)

    return aluno


@router.delete("/api/alunos/{id}", status_code=204)
def apagar_aluno(id: int):
    for aluno in alunos:
        if aluno.id == id:
            alunos.remove(aluno)
            return
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")


@router.put("/api/alunos/{id}")
def editar_aluno(id: int, form: AlunoEditar):
    for aluno in alunos:
        if aluno.id == id:
            aluno.nome = form.nome
            aluno.sobrenome = form.sobrenome
            aluno.cpf = form.cpf
            aluno.data_nascimento = form.data_nascimento
            return aluno
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")