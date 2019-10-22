# Consumindo a SpaceX API com Python / Django / React

Versão da API: 0.1

![spacex_image](https://camo.githubusercontent.com/8caf62499f477b6bf0d3eaff109faff38d5a791e/68747470733a2f2f696d6775722e636f6d2f4a493650754b6c2e706e67)

Primeira versão da API finalizada

**Objetivo:**
Desenvolver uma API em Python que consome a SpaceX API e seja capaz de apresentar as seguintes informações:
	Último Lançamento
	Próximo Lançamento
	Todos os Lançamentos

Desenvolver o frontend em ReactJS para consumir a API criada e apresentar as informações acima.

# Guia da API:

**Todos os Lançamentos**
Para apresentar as informações da SpaceX API deve entrar no link abaixo:

    POST http://localhost:8000/launches/consumption_api/

Observação: Esse processo demora cerca de 10 minutos

**Último lançamento**

    GET http://localhost:8000/launches/latest_consumption/

**Próximo Lançamento**

	GET http://localhost:8000/launches/next_launche/

**Os métodos CREATE, DELETE, UPDATE estão desabilitados para está aplicação.**

Clonando o repositório:

    git clone https://github.com/johannalbino/spaceX_api.git

O projeto é dividido em duas partes/diretórios:

    Frontend (React)
    Backend (Python/Django/RestFramework)

As bibliotecas utilizadas para o desenvolvimento estão disponíveis em:

    package.json - React Library 
    requirements.txt - Python Library


# Instruções

Instalação das bibliotecas ReactJS. Observação: Deve executar o comando no diretório frontend/spacex_app/

    npm install

Instação das bibliotecas do Python. Observação: Deve executar o comando no diretório backend.

    pip install -r requirements.txt

# Ferramentas utilizadas para o desenvolvimento da aplicação:
    Pycharm
    Visual Studio Code