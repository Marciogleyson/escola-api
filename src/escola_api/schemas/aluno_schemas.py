from pydantic import BaseModel, Field
from datetime import datetime

class Aluno(BaseModel):
    id: int = Field()
    nome: str = Field()
    sobrenome: str = Field()
    cpf: str = Field()
    data_nascimento: datetime = Field(alias="dataNascimento")


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