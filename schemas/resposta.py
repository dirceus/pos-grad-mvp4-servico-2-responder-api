from pydantic import BaseModel
from typing import Optional, List
from model.resposta import Resposta


class RespostaSchema(BaseModel):
    """ Define como uma resposta a ser inserida deve ser representadoa
    """
    id_questao: int = 1
    id_usuario: int = 1
    id_alternativa: int = 1


class RespostaViewSchema(BaseModel):
    """ Define como uma resposta será retornada
    """
    mensagem: str = "Questão respondida corretamente"
    id_questao: int = 1
    id_usuario: int = 1
    resultado: bool = True


class QuestaoResponseSchema(BaseModel):
    """ Define a representacao da da ultima questão respondida
    """
    id_questao: int = 1


class UsuarioPath(BaseModel):
    id_usuario: int


def apresenta_id_questao(id_questao: int):
    return {
        "id_questao": id_questao
    }

def apresenta_resposta(resposta: Resposta):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": resposta.id,
        "id_questao": resposta.id_questao,
        "id_usuario": resposta.id_usuario,
        "resultado": resposta.resultado,
    }
