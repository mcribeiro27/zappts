# Teste Zappts (Carta do papai noel - API)

## Apresentação

Este documento é para apresentar o funcionamento da implementação das rotas para cadastro de uma carta para o Papai Noel. Foi realizado em python juntamente com o frameworks FLASK, pois por se tratar de um micro-frameworks, instala-se apenas o necessário.

Tive um pouco de dificuldade com o deploy da api, pois raramente executo este tipo de serviço.

## Autenticação

Esta API está usando como proteção de algumas rotas o JWT.
Para se autenticar é preciso utilizar a seguinte rota:

```url
/carta/login
```

BODY:
```json
{
    "remetente": "Marcos c",
    "password": "123deoliveira4",
}
```
RETORNO:

```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMzYxOTcxMCwianRpIjoiNjg2ZDFhOGYtOGViNS00Y2U4LWJlNTgtODM4ZDljMDNhOTcyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjIzNjE5NzEwLCJleHAiOjE2MjM2MjA2MTB9.dvAXYH9sp4giQG886LYZYxGnhuLBr_k5djI_hastcLY"
}
```
Ao ter o token em mãos é necessário ir em authorization no campo Type seleciona " BEARER TOKEN " e colar o token no campo.

## Começando

Para acessar a api serão necessários os seguites requisitos:

- [Python 3.9: necessário para a execução do sistema](www.python.org/)
- [Postman: necessário para o teste da API](www.postman.com)

## Desenvolvimento

Para iniciar o desenvolvimento, é necessário clonar o projeto do github em um diretório de sua preferência.

```commandline
mkdir "diretório_de_sua_preferência"
cd "diretório_de_sua_preferência"
git clone https://github.com/mcribeiro27/zappts
```

## Construção

Para construir o projeto, execute os comandos abaixo dentro da pasta onde baixou o projeto.

Para ambiente Unix
```commandline
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirement.txt
```

Para ambiente Windows
```commandline
pip install virtualenv
virtualenv venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```
O comando irá montar o ambiente e instalar todos os módulos necessário para  o sistema.

## Configuração

Ao iniciar o sistema teremos que criar o banco de dados, o sistema está configurado para trabalhar com o SQLite.
Para criar o banco execute o seguinte comando:
```commandline
flask create-db
```
Ao executar sera criado o banco. Apartir daí podemos testar os end-points.

### Carta
Através desta rota conseguimos cadastrar, listar, buscar, modificar e apagar uma Carta na API - Carta do Papai Noel

POST - Para cadastro de uma nova carta
```url
/carta
```

BODY:
```json
{
    "cartaId": 1, 
    "remetente": "Marcos c",
    "password": "123deoliveira4",
    "conteudo": "Quero um playstation 5"
}
```
RETORNO:

```json
{
    "cartaId": 1, 
    "remetente": "Marcos c",
    "password": "123deoliveira4",
    "conteudo": "Quero um playstation 5"
}
```
GET - Para listar todas as cartas

```url
/carta
```

RETORNO:

```json
{
    "cartas": [
        {
            "cartaId": 1,
            "remetente": "Marcos c",
            "password": "123deoliveira4",
            "conteudo": "Quero um playstation 5"
        }
    ]
}
```
GET by id - Para buscar uma carta especifica.
```url
/carta/{cartaId}
```
RETORNO:
```json
{
    "cartaId": 1,
    "remetente": "Marcos c",
    "password": "123deoliveira4",
    "conteudo": "Quero um playstation 5"
}
```

PUT - Para atualizar uma carta. Esta rota precisa estar logada para funcionar
```url
/carta/{cartaId}
```
BODY:
```json
{
    "remetente": "Marcos Cesar",
    "password": "123deoliveira4",
    "conteudo": "Quero um playstation 5"
}
```
RETORNO:

```json
{
    "cartaId": 1, 
    "remetente": "Marcos Cesar",
    "password": "123deoliveira4",
    "conteudo": "Quero um playstation 5"
}
```


DELETE - Para apagar uma carta. Esta rota precisa estar logada para funcionar

```url
/carta/{cartaId}
```
RETORNO:
```json
{
    "message": "carta deleted"
}
```

## Testes
Lembrando que o banco de dados deve estar criado. Caso não esteja execute o seguinte comando:

```commandline
flask create-db
```

Todos os testes foram realizados com a biblioteca PYTEST, onde para executar basta rodar no terminal o seguinte comando. 
```commandline
pytest
```