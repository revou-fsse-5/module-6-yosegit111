from flask import Blueprint, jsonify, request
from core.services.employee_service import *
from core.utils.validation import validate_employee_data

employee_blueprint = Blueprint('employee', __name__)

@employee_blueprint.route('/employees', methods=['GET'])
def get_employees():
    employees = get_all_employees()
    return jsonify(employees), 200

@employee_blueprint.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = get_employee_by_id(id)
    return jsonify(employee), 200 if employee else 404

@employee_blueprint.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    errors = validate_employee_data(data)
    if errors:
        return jsonify({"errors": errors}), 400
    new_employee = create_employee(data)
    return jsonify(new_employee), 201

@employee_blueprint.route('/employees/<int:id>', methods=['PUT'])
def update_employee_route(id):
    data = request.get_json()
    employee = update_employee(id, data)
    return jsonify(employee), 200 if employee else 404

@employee_blueprint.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee_route(id):
    delete_employee(id)
    return jsonify({"message": "Employee deleted"}), 200
