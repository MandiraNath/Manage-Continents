from flask import Blueprint, jsonify, request
from app.models import Continent, Country, City
from app.db import db

api_blueprint = Blueprint('api', __name__)

#create continent
@api_blueprint.route('/continents', methods=['POST'])
def create_continent():
    data = request.json
    new_continent = Continent(name=data['name'])
    db.session.add(new_continent)
    db.session.commit()
    return jsonify({"id": new_continent.id, "name": new_continent.name}), 201

#get continent details
@api_blueprint.route('/continents', methods=['GET'])
def list_continents():
    continents = Continent.query.all()
    return jsonify([{"id": c.id, "name": c.name} for c in continents])

#DELETE continent
@api_blueprint.route('/continents/<int:id>', methods=['DELETE'])
def delete_continent(id):
    continent = Continent.query.get(id)
    if continent:
        db.session.delete(continent)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Continent not found"}), 404

#create country with continent ID
@api_blueprint.route('/countries', methods=['POST'])
def create_country():
    data = request.json
    continent = Continent.query.get(data['continent_id'])
    if not continent:
        return jsonify({"error": "Continent not found"}), 404
    new_country = Country(name=data['name'], continent_id=continent.id)
    db.session.add(new_country)
    db.session.commit()
    return jsonify({"id": new_country.id, "name": new_country.name, "continent_id": new_country.continent_id}), 201

#get country details
@api_blueprint.route('/countries', methods=['GET'])
def list_countries():
    countries = Country.query.all()
    return jsonify([{"id": c.id, "name": c.name, "continent_id": c.continent_id} for c in countries])

#delete a country
@api_blueprint.route('/countries/<int:id>', methods=['DELETE'])
def delete_country(id):
    country = Country.query.get(id)
    if country:
        db.session.delete(country)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Country not found"}), 404

#get details of city with COuntry ID
@api_blueprint.route('/countries/<int:id>/cities', methods=['GET'])
def list_cities_in_country(id):
    country = Country.query.get(id)
    if country:
        cities = City.query.filter_by(country_id=country.id).all()
        return jsonify([{"id": city.id, "name": city.name} for city in cities])
    return jsonify({"error": "Country not found"}), 404

#create city with country ID
@api_blueprint.route('/cities', methods=['POST'])
def create_city():
    data = request.json
    country = Country.query.get(data['country_id'])
    if not country:
        return jsonify({"error": "Country not found"}), 404
    new_city = City(name=data['name'], country_id=country.id)
    db.session.add(new_city)
    db.session.commit()
    return jsonify({"id": new_city.id, "name": new_city.name, "country_id": new_city.country_id}), 201

#get details of cities
@api_blueprint.route('/cities', methods=['GET'])
def list_cities():
    cities = City.query.all()
    return jsonify([{"id": city.id, "name": city.name, "country_id": city.country_id} for city in cities])

# Update a continent
@api_blueprint.route('/continents/<int:id>', methods=['PUT'])
def update_continent(id):
    continent = Continent.query.get(id)
    if continent:
        data = request.json
        continent.name = data.get('name', continent.name)
        db.session.commit()
        return jsonify({"id": continent.id, "name": continent.name}), 200
    return jsonify({"error": "Continent not found"}), 404

# Update a country
@api_blueprint.route('/countries/<int:id>', methods=['PUT'])
def update_country(id):
    country = Country.query.get(id)
    if country:
        data = request.json
        country.name = data.get('name', country.name)
        continent_id = data.get('continent_id')
        if continent_id:
            country.continent_id = continent_id
        db.session.commit()
        return jsonify({"id": country.id, "name": country.name, "continent_id": country.continent_id}), 200
    return jsonify({"error": "Country not found"}), 404

# Update a city
@api_blueprint.route('/cities/<int:id>', methods=['PUT'])
def update_city(id):
    city = City.query.get(id)
    if city:
        data = request.json
        city.name = data.get('name', city.name)
        country_id = data.get('country_id')
        if country_id:
            city.country_id = country_id
        db.session.commit()
        return jsonify({"id": city.id, "name": city.name, "country_id": city.country_id}), 200
    return jsonify({"error": "City not found"}), 404

# Delete a city
@api_blueprint.route('/cities/<int:id>', methods=['DELETE'])
def delete_city(id):
    city = City.query.get(id)
    if city:
        db.session.delete(city)
        db.session.commit()
        return jsonify({"message": "City deleted successfully"}), 200
    return jsonify({"error": "City not found"}), 404
