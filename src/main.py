import uvicorn

from src.escola_api.api.v1 import matricula_controller
from src.escola_api.database.banco_dados import Base, engine, popular_banco_dados
from src.escola_api.api.v1 import aluno_controller
from src.escola_api.api.v1 import curso_controller
from src.escola_api.app import app

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
popular_banco_dados()

app.include_router(aluno_controller.router)
app.include_router(curso_controller.router)
app.include_router(matricula_controller.router)

if __name__ == "__main__":
    uvicorn.run("main:app")
