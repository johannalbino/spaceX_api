# Desenvolvimento da SpaceX API com Python/Django e React

![spacex_image](https://camo.githubusercontent.com/8caf62499f477b6bf0d3eaff109faff38d5a791e/68747470733a2f2f696d6775722e636f6d2f4a493650754b6c2e706e67)

API em desenvolvimento

Objetivo:
Elaborar uma API em Python/Django que consuma a API da SpaceX API e seja capaz apresentar as seguintes informações:

	Último Lançamento	
	Próximo Lançamento	
	Todos os Lançamentos

Além disso desenvolver o frontend em React que irá consumir a API criada e apresentar as informações acima.

# Instruções:

**All Launches**
Com esse link você deleta tudo que está no banco de dados e consome a API da SpaceX novamente e armazena no banco de dados novamente:

    POST http://localhost:8000/launches/consumption_api/

Observação: Esse processo pode levar alguns minutos, em média 10 minutos.

**Latest Launche**
Verificar qual o ultimo lançamento

    GET http://localhost:8000/launches/latest_consumption/

**Next Launche**
Retorna o próximo lançamento

	GET http://localhost:8000/launches/next_launche/

**Método CREATE e UPDATE está desativada para está API.**

Clonar repositório:

    git clone https://github.com/johannalbino/spaceX_api.git

O projeto é divido em dois diretórios:

    Frontend (React)
    Backend (Python/Django/RestFramework)

As bibliotecas utilizadas se encontram na pasta de cada módulo:

    package.json - Bibliotecas do React
    requirements.txt - Bibliotecas do Python


Para instalar as bibliotecas do React é só digitar o comando no diretório frontend/spacex_app/:

    npm install

Para instalar as bibliotecas do Python é só digitar o comando no diretório backend:

    pip install -r requirements.txt

# Ferramentas utilizadas para o desenvolvimento:
    Pycharm - IDE para trabalhar com Python/Django
    Visual Studio Code - IDE para trabalhar com React/JS