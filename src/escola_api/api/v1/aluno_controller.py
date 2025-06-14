from fastapi import HTTPException, Query
from fastapi.params import Depends
from sqlalchemy import or_
from sqlalchemy.orm import Session

from src.escola_api.dependencias import get_db
from src.escola_api.app import router
from src.escola_api.database.modelos import AlunoEntidade
from src.escola_api.schemas.aluno_schemas import Aluno, AlunoEditar, AlunoCadastro



@router.get("/api/alunos", tags=["alunos"])
def listar_todos_alunos(filtro: str = Query(default="", alias="filtro"), db: Session = Depends(get_db)):
    pesquisa = f"%{filtro}%"
    alunos = db.query(AlunoEntidade).filter(
        or_(
            AlunoEntidade.nome.ilike(pesquisa),
            AlunoEntidade.sobrenome.ilike(pesquisa),
            # AlunoEntidade.cpf == filtro # buscar exatamente aquele cpf "210.202.131-22"
            AlunoEntidade.cpf.ilike(f"{filtro}%") # buscar o cpf que começa com "210"
            # AlunoEntidade.cpf.ilike(pesquisa) # busca em qualquer part do cpf
        )
    ).all()
    alunos_response = [Aluno(
        id=aluno.id,
        nome=aluno.nome,
        sobrenome=aluno.sobrenome,
        cpf=aluno.cpf,
        data_nascimento=aluno.data_nascimento,
    ) for aluno in alunos]
    return alunos_response


@router.get("/api/alunos/{id}", tags=["alunos"])
def obter_por_id_alunos(id: int, db: Session = Depends(get_db)):
    aluno = db.query(AlunoEntidade).filter(AlunoEntidade.id == id).first()
    if aluno:
        return Aluno(
            id=aluno.id,
            nome=aluno.nome,
            sobrenome=aluno.sobrenome,
            cpf=aluno.cpf,
            data_nascimento=aluno.data_nascimento,
        )
    # Lançando uma exceção com o status code de 404(não encontrado)
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")


@router.post("/api/alunos", tags=["alunos"])
def cadastrar_aluno(form: AlunoCadastro, db: Session = Depends(get_db)):
    # instanciar um objeto da classe AlunoEntidade
    aluno = AlunoEntidade(
        nome=form.nome,
        sobrenome=form.sobrenome,
        cpf=form.cpf,
        data_nascimento=form.data_nascimento)

    db.add(aluno)
    db.commit()
    db.refresh(aluno)

    return aluno


@router.delete("/api/alunos/{id}", tags=["alunos"] , status_code=204)
def apagar_aluno(id: int, db: Session = Depends(get_db)):
    aluno = db.query(AlunoEntidade).filter(AlunoEntidade.id == id).first()
    if aluno:
        db.delete(aluno)
        db.commit()
        return
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")


@router.put("/api/alunos/{id}", tags=["alunos"])
def editar_aluno(id: int, form: AlunoEditar, db: Session = Depends(get_db)):
    aluno = db.query(AlunoEntidade).filter(AlunoEntidade.id == id).first()
    if aluno:
        aluno.nome = form.nome
        aluno.sobrenome = form.sobrenome
        aluno.cpf = form.cpf
        aluno.data_nascimento = form.data_nascimento
        db.commit()
        db.refresh(aluno)
        return aluno
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")
