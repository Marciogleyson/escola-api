from sqlalchemy import Column, String, Integer

from src.escola_api.database.banco_dados import Base


class CursoEntidade(Base):
    __tablename__ = 'curso'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    sigla = Column(String(3), nullable=False)