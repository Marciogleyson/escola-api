from src.escola_api.app import router


@router.get("/api/matriculas", status_code=200, tags=["matriculas"])
def lista_todos_matriculas():
    pass


@router.post("/api/matriculas", status_code=200, tags=["matriculas"])
def cadastrar_matriculas():
    pass


@router.delete("/api/matriculas", status_code=204, tags=["matriculas"])
def apagar_matriculas():
    pass


@router.put("/api/matriculas", status_code=204, tags=["matriculas"])
def editar_matriculas():
    pass


@router.get("/api/matriculas", status_code=204, tags=["matriculas"])
def obter_por_id_matricula():
    pass