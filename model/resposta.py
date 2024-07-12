from sqlalchemy import Column, String, Integer, DateTime, Float, Boolean
from datetime import datetime
from typing import Union

from model import Base


class Resposta(Base):
    __tablename__ = 'resposta'

    id = Column("pk_resposta", Integer, primary_key=True)
    id_questao = Column(Integer)
    id_usuario = Column(Integer)
    resultado = Column(Boolean)
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, id_questao:int,id_usuario:int, resultado:bool,
                 data_insercao:Union[DateTime, None] = None):
        """
        Resgistra uma Resposta

        Arguments:
            id_questao: identificador da questão que foi respondida.
            id_usuario: identificador da usuário que respondeu a questão.
            resultado: resultado se a questão foi respondida corretamente
            data_insercao: data de quando a questão foi respondida
        """
        self.id_questao = id_questao
        self.id_usuario = id_usuario
        self.resultado = resultado

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao