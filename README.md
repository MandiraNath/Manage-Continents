# Manage-Continents
This application will expose a REST API to manage (Create, Read, Update, Delete) Continents, Countries and Cities

Steps to start the application :
1. start Docker
2. Run command  -> docker-compose up --build
3. API will be available with -> http://localhost:5000/api/

Below are the API detailsa along with input:

Create:
Continent : POST http://localhost:5000/api/continents -> {"name": "Europe"}
Contries : POST http://localhost:5000/api/countries  -> {"name": "France", "continent_id": 1}
Cities: POST http://localhost:5000/api/cities -> {"name": "Paris", "country_id": 1}

Read:
Continent : GET http://localhost:5000/api/continents 
Contries : GET http://localhost:5000/api/countries  , 
Cities: GET http://localhost:5000/api/countries/<country_id>/cities

Delete:
Continent : DELETE http://localhost:5000/api/continents/<id>
Contries : DELETE http://localhost:5000/api/countries/<id>