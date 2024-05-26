from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object('config.Config')

login_manager = LoginManager()
login_manager.init_app(app)

from app.routes import bp as routes_bp  # Import the blueprint from routes.py

app.register_blueprint(routes_bp)  # Register the blueprint

# Rest of your code...pp)

import os  # Import the os module

import sys  # Import the sys module

def create_app():
    # Supabase setup
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')

    # Add the path to your project to sys.path
    sys.path.append('/Users/anarvvasavada/Documents/projects')

    # Import the User class after the app has been created
    from app.models import User

    return app

# Import routes after the app has been created
from app import routes
from supabase import create_client
from app.models import User

app.register_blueprint(routes.bp)
@login_manager.user_loader
def load_user(user_id):
    supabase_url = os.getenv('postgres.rszacpjtzkqiajlyugya password=[YOUR-PASSWORD] host=aws-0-ap-south-1.pooler.supabase.com port=5432 dbname=postgres')
    supabase_key = os.getenv('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJzemFjcGp0emtxaWFqbHl1Z3lhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxNjY2ODUxOCwiZXhwIjoyMDMyMjQ0NTE4fQ.zR_Kel4A24KbSp838UPOVDATgD4q9vBav6ts37BZsVc')
    supabase = create_client(supabase_url, supabase_key)  # Create a supabase client
    response = supabase.table('users').select('*').eq('id', user_id).execute()
    if response.data:
        return User(**response.data[0])
    return None
