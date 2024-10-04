from flask import Flask, render_template, request, redirect, url_for
from core.services.animal_service import get_all_animals, create_animal, update_animal, delete_animal, get_animal_by_id
from core.services.employee_service import get_all_employees, create_employee, update_employee, delete_employee, get_employee_by_id
from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/animals')
def animal_page():
    animals = get_all_animals(supabase)
    return render_template('animals.html', title='Animals', animals=animals, enumerate=enumerate)

@app.route('/employees')
def employee_page():
    employees = get_all_employees(supabase)
    return render_template('employees.html', title='Employees', employees=employees, enumerate=enumerate)

# Form handling for adding animals
@app.route('/add_animal', methods=['POST'])
def add_animal():
    name = request.form['name']
    species = request.form['species']
    age = request.form['age']
    gender = request.form['gender']
    area_code = request.form['area_code']
    
    data = {
        'name': name,
        'species': species,
        'age': int(age),
        'gender': gender,
        'area_code': area_code
    }
    
    create_animal(supabase, data)
    return redirect(url_for('animal_page'))

# Form handling for adding employees
@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    role = request.form['role']
    schedule = request.form['schedule']
    
    data = {
        'name': name,
        'email': email,
        'phone_number': phone_number,
        'role': role,
        'schedule': schedule
    }
    
    create_employee(supabase, data)
    return redirect(url_for('employee_page'))

# Update animal
@app.route('/update_animal/<int:id>', methods=['GET', 'POST'])
def update_animal_route(id):
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']
        gender = request.form['gender']
        area_code = request.form['area_code']

        data = {
            'name': name,
            'species': species,
            'age': int(age),
            'gender': gender,
            'area_code': area_code
        }
        
        update_animal(supabase, id, data)
        return redirect(url_for('animal_page'))
    else:
        animal = get_animal_by_id(supabase, id)
        return render_template('update_animal.html', animal=animal)

# Delete animal
@app.route('/delete_animal/<int:id>')
def delete_animal_route(id):
    delete_animal(supabase, id)
    return redirect(url_for('animal_page'))

# Update employee
@app.route('/update_employee/<int:id>', methods=['GET', 'POST'])
def update_employee_route(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        role = request.form['role']
        schedule = request.form['schedule']

        data = {
            'name': name,
            'email': email,
            'phone_number': phone_number,
            'role': role,
            'schedule': schedule
        }
        
        update_employee(supabase, id, data)
        return redirect(url_for('employee_page'))
    else:
        employee = get_employee_by_id(supabase, id)
        return render_template('update_employee.html', employee=employee)

# Delete employee
@app.route('/delete_employee/<int:id>')
def delete_employee_route(id):
    delete_employee(supabase, id)
    return redirect(url_for('employee_page'))

if __name__ == '__main__':
    app.run(debug=True)
