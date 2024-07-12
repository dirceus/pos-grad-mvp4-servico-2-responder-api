import requests


#método para verificar se a resposta informada foi a correta
def verificar_resposta(id_questao, id_alternativa):
    try:
        #obter questão do microserviço de gestão de questões
        url = 'http://127.0.0.1:5000/api/questao/exibir/' + str(id_questao)
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            questao_dict = response.json()

            alternativas = questao_dict['alternativas']
            alternativa_correta = False
            #checa se resposta informada foi a correta
            for alternativa in alternativas:
                if alternativa['is_correta']:
                    if alternativa['codigo'] == id_alternativa:
                        alternativa_correta = True
                        break
            return alternativa_correta
        else:
            raise Exception(f"Não foi possível verificar a resposta da questão: '{id_questao}")

    except Exception as e:
        # Se ocorrer algum erro inesperado
        raise Exception(f"Não foi possível verificar a resposta da questão: '{id_questao}")


def registrar_pontuacao(id_usuario):
    try:
        #faz requisição para o microserviço de gameficacao // TODO: no futuro substituir por mensageria
        url = 'http://127.0.0.1:5002/api/pontuar_acerto'
        data = {
            "id_usuario": id_usuario,
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"pontos registrados com sucesso para o usuário: '{id_usuario}'")
        else:
            print(f"ocorreu um erro ao registar os pontos para o usuário: '{id_usuario}'")

    except Exception as e:
        print(e)
        print(f"Ocorreu um erro ao registar os pontos para o usuário: '{id_usuario}'")