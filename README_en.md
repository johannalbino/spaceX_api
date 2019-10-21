# SpaceX API-consuming application in Python / Django / React

Version: 0.1

![spacex_image](https://camo.githubusercontent.com/8caf62499f477b6bf0d3eaff109faff38d5a791e/68747470733a2f2f696d6775722e636f6d2f4a493650754b6c2e706e67)

API under development

**Objective:**
Develop a Python API that consumes the SpaceX API and is capable of presenting the following information:

	Latest Launche	
	Next Launche	
	All Launches

Develop the application front end in the ReactJS programming language to consume the created API and present the above information.

# API Guide:

**All Launches**
Deletes everything in the database and consumes the SpaceX API storing in the database again:

    POST http://localhost:8000/launches/consumption_api/

Note: This process may take a few minutes, on average 10 minutes.

**Latest Launche**

    GET http://localhost:8000/launches/latest_consumption/

**Next Launche**

	GET http://localhost:8000/launches/next_launche/

**CREATE, DELETE, UPDATE methods are disabled in this application.**

Clone repository:

    git clone https://github.com/johannalbino/spaceX_api.git

The project is division in two parts/directory:

    Frontend (React)
    Backend (Python/Django/RestFramework)

The libraries used are in the folder of each module:

    package.json - React Library 
    requirements.txt - Python Library


# Instructions

ReactJS libraries installation. Note: Must do this in the directory frontend/spacex_app/

    npm install

Python libraries installation. Note: Must do this in the directory backend.

    pip install -r requirements.txt

# Tools used for application development:
    Pycharm
    Visual Studio Code