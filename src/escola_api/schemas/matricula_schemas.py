
from datetime import date

from pydantic import BaseModel, Field


class MatriculaBase(BaseModel):
    aluno_id: int = Field()
    curso_id: int = Field()

#Listagem, obter por id (get)
class Matricula(MatriculaBase):
    data_matricula: date = Field(alias="dataMatricula")

# cadastro (post)
class MatriculaCadastro(MatriculaBase):
   pass

class MatriculaEditar(BaseModel):
    curso_id: int = Field()