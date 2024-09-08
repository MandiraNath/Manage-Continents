from flask import Blueprint, jsonify, request
from app.models import Continent, Country, City
from app.db import db

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/continents', methods=['POST'])
def create_continent():
    data = request.json
    new_continent = Continent(name=data['name'])
    db.session.add(new_continent)
    db.session.commit()
    return jsonify({"id": new_continent.id, "name": new_continent.name}), 201

@api_blueprint.route('/continents', methods=['GET'])
def list_continents():
    continents = Continent.query.all()
    return jsonify([{"id": c.id, "name": c.name} for c in continents])

@api_blueprint.route('/continents/<int:id>', methods=['DELETE'])
def delete_continent(id):
    continent = Continent.query.get(id)
    if continent:
        db.session.delete(continent)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Continent not found"}), 404

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

@api_blueprint.route('/countries', methods=['GET'])
def list_countries():
    countries = Country.query.all()
    return jsonify([{"id": c.id, "name": c.name, "continent_id": c.continent_id} for c in countries])

@api_blueprint.route('/countries/<int:id>', methods=['DELETE'])
def delete_country(id):
    country = Country.query.get(id)
    if country:
        db.session.delete(country)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Country not found"}), 404

@api_blueprint.route('/countries/<int:id>/cities', methods=['GET'])
def list_cities_in_country(id):
    country = Country.query.get(id)
    if country:
        cities = City.query.filter_by(country_id=country.id).all()
        return jsonify([{"id": city.id, "name": city.name} for city in cities])
    return jsonify({"error": "Country not found"}), 404

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

@api_blueprint.route('/cities', methods=['GET'])
def list_cities():
    cities = City.query.all()
    return jsonify([{"id": city.id, "name": city.name, "country_id": city.country_id} for city in cities])
