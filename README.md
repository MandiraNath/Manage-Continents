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
Continent : GET http://localhost:5000/api/continents ,
Contries : GET http://localhost:5000/api/countries  , 
All cities: GET http://localhost:5000/api/cities ,
Cities with country ID: GET http://localhost:5000/api/countries/<country_id>/cities


Update:
Continent : PUT http://localhost:5000/api/continents/<continent_ID>  -> {"name": "Updated Continent Name"}  ,
Contries : PUT http://localhost:5000/api/countries/<country_ID> ->{"name": "updated country name"}  , 
Cities: PUT http://localhost:5000/api/cities/<city_id>  -> {"name": "Updated City Name", "country_id": <country_id>}

Delete:
Continent : DELETE http://localhost:5000/api/continents/<id>
Contries : DELETE http://localhost:5000/api/countries/<id>
City: DELETE http://localhost:5000/api/cities/<id>