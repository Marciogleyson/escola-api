from datetime import date
from operator import index

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.escola_api.database.banco_dados import Base


class CursoEntidade(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    sigla = Column(String(3), nullable=False)

# from datetime import datetime
# from sqlalchemy import Column, Integer, String, DateTime
# from src.escola_api.database.banco_dados import Base

class AlunoEntidade(Base):
    __tablename__ = "alunos"

    id: int =  Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(20), nullable=False)
    sobrenome: str = Column(String(50), nullable=False)
    cpf: str = Column(String(14), nullable=False)
    data_nascimento: date = Column(Date(), nullable=False, name="data_nascimento")


class MatriculaEntidade(Base):
    __tablename__ = "matriculas"

    id: int = Column(Integer, primary_key=True, index=True)
    aluno_id: int = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    curso_id: int = Column(Integer, ForeignKey(CursoEntidade.id), nullable=False)
    data_matricula: date = Column(Date, nullable=False, default=date.today)

    #Relacionamento
   # aluno = relationship("AlunoEntidade", back_populates="matriculas")
   # curso = relationship("CursoEntidade", back_populates="matriculas")