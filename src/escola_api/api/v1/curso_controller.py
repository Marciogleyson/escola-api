from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from src.escola_api.database.banco_dados import SessionLocal
from src.escola_api.database.modelos import CursoEntidade
from src.escola_api.schemas.curso_schemas import Curso, CursoEditar, CursoCadastro
from src.escola_api.app import router

cursos = [
    # instanciando um objeto da Class Curso
    Curso(id=1, nome="Python Web", sigla="PY1"),
    Curso(id=2, nome="Git e GitHub", sigla="GT")
]

#Função de dependência para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal() # cria uma nova sessão no banco de dados
    try:
        yield db # Retorna a sessão de forma que o FastAPI possa utilizá-la nas rotas
    finally:
        db.close() # Garante que a sessão será fechada após o uso



@router.get("/api/cursos")
def listar_todos_cursos(db: Session = Depends(get_db)):
    cursos = db.query(CursoEntidade).all()
    return cursos


@router.get("/api/cursos/{id}")
def obter_por_id_curso(id: int, db: Session = Depends(get_db)):
    curso = db.query(CursoEntidade).filter(CursoEntidade.id == id).first()
    if curso:
      return curso

    # Lançando uma exceção com o status code de 404(não encontrado)
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@router.post("/api/cursos")
def cadastrar_curso(form: CursoCadastro, db: Session = Depends(get_db)):

    # instanciar um objeto da classe Curso
    curso = CursoEntidade( nome=form.nome, sigla=form.sigla)
    db.add(curso)  #insert
    db.commit() # Efetivando o registro na tabela
    db.refresh(curso)  # preencher o id que foi gerado no banco de dados

    return curso


@router.delete("/api/cursos/{id}", status_code=204)
def apagar_curso(id: int, db: Session = Depends(get_db)):
    curso = db.query(CursoEntidade).filter(CursoEntidade.id == id).first()
    if curso:
        db.delete(curso)
        db.commit()
        return
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@router.put("/api/cursos/{id}")
def editar_curso(id: int, form: CursoEditar, db: Session = Depends(get_db)):
    curso = db.query(CursoEntidade).filter(CursoEntidade.id == id).first()
    if curso:
        curso.nome = form.nome
        curso.sigla = form.sigla
        db.commit()
        return curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")