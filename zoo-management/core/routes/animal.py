from flask import Blueprint, jsonify, request
from core.services.animal_service import *
from core.utils.validation import validate_animal_data

animal_blueprint = Blueprint('animal', __name__)

@animal_blueprint.route('/animals', methods=['GET'])
def get_animals():
    animals = get_all_animals()
    return jsonify(animals), 200

@animal_blueprint.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    animal = get_animal_by_id(id)
    return jsonify(animal), 200 if animal else 404

@animal_blueprint.route('/animals', methods=['POST'])
def add_animal():
    data = request.get_json()
    errors = validate_animal_data(data)
    if errors:
        return jsonify({"errors": errors}), 400
    new_animal = create_animal(data)
    return jsonify(new_animal), 201

@animal_blueprint.route('/animals/<int:id>', methods=['PUT'])
def update_animal_route(id):
    data = request.get_json()
    animal = update_animal(id, data)
    return jsonify(animal), 200 if animal else 404

@animal_blueprint.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal_route(id):
    delete_animal(id)
    return jsonify({"message": "Animal deleted"}), 200
