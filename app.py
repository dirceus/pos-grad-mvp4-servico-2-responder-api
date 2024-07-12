from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

from model import Session, Resposta
from logger import logger
from schemas import *
from flask_cors import CORS

from schemas.resposta import RespostaViewSchema, apresenta_resposta, QuestaoResponseSchema, UsuarioPath, \
    apresenta_id_questao
from business.reposta import verificar_resposta, registrar_pontuacao

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
resposta_tag = Tag(name="Resposta", description="Inclusão de Respostas e consulta de historica de questões respondidas")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/resposta', tags=[resposta_tag],
          responses={"200": RespostaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_resposta(body: RespostaSchema):
    """Registra uma resposta de uma questão

    Retorna retorna o resultado da resposta.
    """
    logger.debug(f"verificando se a resposta está correta")
    resultado_resposta = verificar_resposta(body.id_questao, body.id_alternativa)
    resp = Resposta(
        id_questao=body.id_questao,
        id_usuario=body.id_usuario,
        resultado=resultado_resposta)
    logger.debug(f"Registrando uma resposta do usário '{resp.id_usuario}' para a questão: '{resp.id_questao}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando resposta
        session.add(resp)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(
            f"Registrado uma resposta do usário '{resp.id_usuario}' para a questão: '{resp.id_questao}'")
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar a resposta do usuário item :/"
        logger.warning(f"Erro ao registrar resposta da questao '{resp.id_questao}', {error_msg}")
        return {"mesage": error_msg}, 400
    try:
        if resultado_resposta :
            registrar_pontuacao(resp.id_usuario)
    except Exception as e:
        logger.warning(e)
        logger.warning(f"Erro ao pontuação do usuário '{resp.id_usuario}'")

    return apresenta_resposta(resp), 200


@app.get('/ultima_questao_respondida/<int:id_usuario>', tags=[resposta_tag],
         responses={"200": QuestaoResponseSchema, "400": ErrorSchema, "500": ErrorSchema})
def obter_ultima_questao(path: UsuarioPath):

    """Obtem o id da ultima questão respondida
    """
    try:
        # criando conexão com a base
        session = Session()
        max_id = session.query = session.query(func.max(Resposta.id_questao)).filter_by(id_usuario=path.id_usuario).scalar()
        print(max_id)
        if max_id == None:
            max_id = 0
        return apresenta_id_questao(max_id)
    except Exception as ex:
        return apresenta_id_questao(0)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)