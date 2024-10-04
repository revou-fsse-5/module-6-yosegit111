from supabase import create_client, Client
import os

# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_all_animals(supabase):
    response = supabase.table('animals').select('*').execute()
    return response.data

def get_animal_by_id(supabase, id):
    response = supabase.table('animals').select('*').eq('id', id).execute()
    return response.data[0] if response.data else None

def create_animal(supabase, data):
    response = supabase.table('animals').insert(data).execute()
    return response.data[0]

def update_animal(supabase, id, data):
    response = supabase.table('animals').update(data).eq('id', id).execute()
    return response.data[0] if response.data else None

def delete_animal(supabase, id):
    supabase.table('animals').delete().eq('id', id).execute()
    return True
