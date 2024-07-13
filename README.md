# pos-grad-mvp4-respondarapido-api
Esse componente faz parte do MVP da disciplina de Arquitetura de Software do cursos de Pós Graduação em Engenhiria de software.

## Objetivo
Objetivo desse componente é fornecer uma API para responder questões e verificar se a questão foi respondida corretamente.

## Tecnlogias

* Pyhon
* Flask
* SQLite

## Arquitetura

![image](https://github.com/user-attachments/assets/caf01713-2404-4814-a988-8c5ea26f8232)


Para mais informações sobre arquitetura do MVP consultar: https://github.com/dirceus/pos-grad-mvp4-servico_principal-frontend

## Dependências

Ele possui como dependência dos componentes:

* API de Questões: https://github.com/dirceus/pos-grad-mvp4-servico-1-questao-api
* API de Gameficação: https://github.com/dirceus/pos-grad-mvp4-servico-3-gameficacao-api.git

Frontend desse componente: 
https://github.com/dirceus/pos-grad-mvp4-servico_principal-frontend

## Como executar localmente esse componente


    Baixe ou clone este repositório usando git clone

    Crie um ambiente virtual do tipo virtualenv.

    No ambiente virtual, instale as dependências através do comando:

```(env)$ pip install -r requirements.txt ```

    Execute a API através do comando

```(env)$ flask run --host 0.0.0.0 --port 5001 ```

    Com a aplicação rodando, abra no navegador a url: http://localhost:5001/#/
