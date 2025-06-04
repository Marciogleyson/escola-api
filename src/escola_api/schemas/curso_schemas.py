from typing import Optional
from pydantic import BaseModel, Field


class Curso(BaseModel):
    id: int = Field()
    nome: str = Field()
    sigla: Optional[str] = Field(default=None)


class CursoCadastro(BaseModel):
    nome: str = Field()
    sigla: Optional[str] = Field(default=None)


class CursoEditar(BaseModel):
    nome: str = Field()
    sigla: Optional[str] = Field(default=None)