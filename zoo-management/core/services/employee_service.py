from supabase import create_client, Client
import os

# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_all_employees(supabase):
    response = supabase.table('employees').select('*').execute()
    return response.data

def get_employee_by_id(supabase, id):
    response = supabase.table('employees').select('*').eq('id', id).execute()
    return response.data[0] if response.data else None

def create_employee(supabase, data):
    response = supabase.table('employees').insert(data).execute()
    return response.data[0]

def update_employee(supabase, id, data):
    response = supabase.table('employees').update(data).eq('id', id).execute()
    return response.data[0] if response.data else None

def delete_employee(supabase, id):
    supabase.table('employees').delete().eq('id', id).execute()
    return True

