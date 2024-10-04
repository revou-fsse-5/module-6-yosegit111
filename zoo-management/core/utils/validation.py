def validate_animal_data(data):
    errors = []
    if not isinstance(data.get('name'), str):
        errors.append('Name must be a string.')
    if not isinstance(data.get('species'), str):
        errors.append('Species must be a string.')
    if not isinstance(data.get('age'), int):
        errors.append('Age must be a number.')
    if data.get('gender') not in ['Male', 'Female']:
        errors.append('Gender must be Male or Female.')
    if not isinstance(data.get('area_code'), str):
        errors.append('Area code must be a string.')
    return errors

def validate_employee_data(data):
    errors = []
    if not isinstance(data.get('name'), str):
        errors.append('Name must be a string.')
    if not isinstance(data.get('email'), str):
        errors.append('Email must be a string.')
    if not isinstance(data.get('phone_number'), str):
        errors.append('Phone number must be a string.')
    if not isinstance(data.get('role'), str):
        errors.append('Role must be a string.')
    if not isinstance(data.get('schedule'), str):
        errors.append('Schedule must be a string consiting of Day Shift (Morning, Afternoon, Evening). Example: Monday Morning')
    return errors
