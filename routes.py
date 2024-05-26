from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from supabase import create_client, Client
import os
from utils import create_predefined_tokens, validate_email, validate_eth_address
from models import User
from flask import current_app as app
bp = Blueprint('routes', __name__)

# Supabase setup
supabase_url = os.getenv('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJzemFjcGp0emtxaWFqbHl1Z3lhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTY2Njg1MTgsImV4cCI6MjAzMjI0NDUxOH0.IlCEHILZng2jtnV0dDIDx0WcoxPO9Z2aLraIzt-iUeQ')
supabase_key = os.getenv('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJzemFjcGp0emtxaWFqbHl1Z3lhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxNjY2ODUxOCwiZXhwIjoyMDMyMjQ0NTE4fQ.zR_Kel4A24KbSp838UPOVDATgD4q9vBav6ts37BZsVc')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('routes.index'))
            else:
                return "Invalid credentials", 400
        else:
            return "User not found", 404
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)