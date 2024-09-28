from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import db, Contact
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/solutions')
def solutions():
    return render_template('solutions.html')

@main_bp.route('/use-cases')
def use_cases():
    return render_template('use_cases.html')

@main_bp.route('/resources')
def resources():
    return render_template('resources.html')

@main_bp.route('/technology')
def technology():
    return render_template('technology.html')

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()
        
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('main.contact'))
    
    return render_template('contact.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username, now=datetime.now())
