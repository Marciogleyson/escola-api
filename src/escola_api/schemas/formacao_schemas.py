from typing import Optional

from pydantic import BaseModel, Field


class Formacao(BaseModel):
    id: int = Field()
    nome: str = Field()
    descricao: Optional[str] = Field()
    duracao: int = Field()


class FormacaoCadastro(BaseModel):
    nome: str = Field()
    descricao: Optional[str] = Field()
    duracao: int = Field()


class FormacaoEditar(BaseModel):
    descricao: Optional[str] = Field()
