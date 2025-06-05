from fastapi import HTTPException

from src.escola_api.app import router
from src.escola_api.schemas.formacao_schemas import Formacao, FormacaoCadastro, FormacaoEditar

formacoes = [
    # instanciando um objeto da Class Formação
    Formacao(id=1, nome="Direito", descricao="curso completo", duracao="5"),
    Formacao(id=2, nome="Engenharia Civil", descricao="curso completo", duracao="4")
]


@router.get("/api/formacoes")
def listar_todas_formacoes():
    return formacoes


@router.get("/api/formacoes/{id}")
def obter_por_id_formacao(id: int):
    for formacao in formacoes:
        if formacao.id == id:
            return formacao

    # Lançando uma exceção com o status code de 404(não encontrado)
    raise HTTPException(status_code=404, detail=f"Formação não encontrada com id: {id}")


@router.post("/api/formacoes")
def cadastrar_formacao(form: FormacaoCadastro):
    ultimo_id = max([formacao.id for formacao in formacoes], default=0)

    # instanciar um objeto da classe Formação
    formacao = Formacao(id=ultimo_id + 1, nome=form.nome, descricao=form.descricao, duracao=form.duracao)

    formacoes.append(formacao)

    return formacao


@router.delete("/api/formacoes/{id}", status_code=204)
def apagar_curso(id: int):
    for formacao in formacoes:
        if formacao.id == id:
            formacoes.remove(formacao)
            return
    raise HTTPException(status_code=404, detail=f"Formação não encontrado com id: {id}")


@router.put("/api/formacoes/{id}")
def editar_formacao(id: int, form: FormacaoEditar):
    for formacao in formacoes:
        if formacao.id == id:
            formacao.descricao = form.decricao
            return formacao
    raise HTTPException(status_code=404, detail=f"Formação não encontrado com id: {id}")
