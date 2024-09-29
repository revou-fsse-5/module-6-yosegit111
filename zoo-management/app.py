from flask import Flask, jsonify, request
from supabase import create_client, Client
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# @app.route('/animals', methods=['GET'])
# def get_animals():
#     response = requests.get('https://fakeapi.platzi.com/en/rest/products/')
#     if response.status_code == 200:
#         animals = response.json()
#         return jsonify(animals), 200
#     return jsonify({"error": "Unable to fetch animals"}), 500

# @app.route('/animals/<int:id>', methods=['GET'])
# def get_animal_by_id(id):
#     response = requests.get(f'https://fakeapi.platzi.com/en/rest/products/{id}')
#     if response.status_code == 200:
#         animal = response.json()
#         return jsonify(animal), 200
#     return jsonify({"error": "Animal not found"}), 404

# Get all animals
@app.route('/animals', methods=['GET'])
def get_animals():
    animals = supabase.table('animals').select('*').execute()
    return jsonify(animals.data), 200

# Add a new animal
@app.route('/animals', methods=['POST'])
def add_animal():
    data = request.get_json()
    new_animal = supabase.table('animals').insert({
        'name': data['name'],
        'species': data['species'],
        'area_code': data['area_code'],
        'showing_shift': data['showing_shift'],
        'cage_shift': data['cage_shift']
    }).execute()
    return jsonify(new_animal.data), 201

# Update an animal by ID
@app.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    data = request.get_json()
    updated_animal = supabase.table('animals').update({
        'name': data['name'],
        'species': data['species'],
        'area_code': data['area_code'],
        'showing_shift': data['showing_shift'],
        'cage_shift': data['cage_shift']
    }).eq('id', id).execute()
    return jsonify(updated_animal.data), 200

# Delete an animal by ID
@app.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    supabase.table('animals').delete().eq('id', id).execute()
    return jsonify({"message": "Animal deleted"}), 200

# Get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = supabase.table('employees').select('*').execute()
    return jsonify(employees.data), 200

# Add a new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = supabase.table('employees').insert({
        'name': data['name'],
        'email': data['email'],
        'phone_number': data['phone_number'],
        'role': data['role'],
        'schedule': data['schedule']
    }).execute()
    return jsonify(new_employee.data), 201

# Update an employee by ID
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    updated_employee = supabase.table('employees').update({
        'name': data['name'],
        'email': data['email'],
        'phone_number': data['phone_number'],
        'role': data['role'],
        'schedule': data['schedule']
    }).eq('id', id).execute()
    return jsonify(updated_employee.data), 200

# Delete an employee by ID
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    supabase.table('employees').delete().eq('id', id).execute()
    return jsonify({"message": "Employee deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
