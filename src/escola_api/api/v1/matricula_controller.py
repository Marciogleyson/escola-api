from datetime import date

from fastapi import Depends, HTTPException, Query
from sqlalchemy.orm import Session

from src.escola_api.database.modelos import MatriculaEntidade
from src.escola_api.dependencias import get_db
from src.escola_api.schemas.matricula_schemas import MatriculaEditar, MatriculaCadastro, Matricula, MatriculaAluno
from src.escola_api.app import router


@router.get("/api/matriculas", status_code=200, tags=["matriculas"])
def lista_todos_matriculas(id_curso: int = Query(alias="idCurso"),db: Session = Depends(get_db)):
    matriculas = db.query(MatriculaEntidade).filter(MatriculaEntidade.curso_id == id_curso).all()
    return [Matricula(
        id=matricula.id,
        aluno_id=matricula.aluno_id,
        aluno=MatriculaAluno(
            id=matricula.aluno.id,
            nome=matricula.aluno.nome,
            sobrenome=matricula.aluno.sobrenome
        ),

        curso_id=matricula.curso_id,
        dataMatricula=matricula.data_matricula,
    ) for matricula in matriculas]



@router.post("/api/matriculas", status_code=200, tags=["matriculas"])
def cadastrar_matriculas(form: MatriculaCadastro, db: Session = Depends(get_db)):
    matricula = MatriculaEntidade(
        aluno_id=form.aluno_id,
        curso_id=form.curso.id,
        data_matricula=date.today()
    )

    db.add(matricula)
    db.commit()
    db.refresh(matricula)
    return  matricula


@router.delete("/api/matriculas", status_code=204, tags=["matriculas"])
def apagar_matriculas(id: int, db: Session = Depends(get_db)):
    matricula = db.query(MatriculaEntidade).filter(MatriculaEntidade.id == id).first()
    if matricula:
        db.delete(matricula)
        db.commit()
        return
    raise HTTPException(status_code=404, detail=f"Matricula não encontrada com id {id}")


@router.put("/api/matriculas/{id}", status_code=200, tags=["matriculas"])
def editar_matriculas(id: int, form: MatriculaEditar, db: Session = Depends(get_db)):
    matricula = db.query(MatriculaEntidade).get(id)

    if matricula:
        matricula.curso_id = form.curso_id
        db.commit()
        db.refresh(matricula)
        return matricula
    raise HTTPException(status_code=404, detail=f"Matricula não encontrada com id {id}")



@router.get("/api/matriculas/{id}", status_code=200, tags=["matriculas"])
def obter_por_id_matricula(id: int, db: Session = Depends(get_db)):
    matricula = db.query(MatriculaEntidade).get(id)
    if matricula:
        return  matricula
    raise HTTPException(status_code=404, detail=f"Matricula não encontrada com id {id}")