from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from models import db, Contact
from datetime import datetime
from ai_api import detect_deepfake, get_supported_platforms
from werkzeug.utils import secure_filename
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    supported_platforms = get_supported_platforms()
    return render_template('index.html', supported_platforms=supported_platforms)

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

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@main_bp.route('/update_profile', methods=['POST'])
@login_required
def update_profile():
    if request.method == 'POST':
        current_user.username = request.form.get('username')
        current_user.email = request.form.get('email')
        db.session.commit()
        flash('Your profile has been updated successfully!', 'success')
        return redirect(url_for('main.profile'))

@main_bp.route('/detect_deepfake', methods=['POST'])
def detect_deepfake_route():
    url = request.form.get('url')
    file = request.files.get('file')
    
    if not url and not file:
        return jsonify({"error": "No URL or file provided"}), 400
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', filename)
        file.save(file_path)
        result = detect_deepfake(file_path)
        os.remove(file_path)  # Remove the file after analysis
    else:
        result = detect_deepfake(url)
    
    return jsonify(result)

@main_bp.route('/demos')
def demos():
    return render_template('demos.html')

@main_bp.route('/demo_kyc', methods=['POST'])
def demo_kyc():
    # Simulate KYC verification process
    name = request.form.get('name')
    id_number = request.form.get('id_number')
    # In a real scenario, you would perform actual verification here
    is_verified = len(name) > 3 and len(id_number) > 5
    return jsonify({"verified": is_verified})

@main_bp.route('/demo_media_verification', methods=['POST'])
def demo_media_verification():
    # Simulate media verification process
    url = request.form.get('url')
    # In a real scenario, you would perform actual verification here
    is_authentic = len(url) > 10 and '.' in url
    return jsonify({"authentic": is_authentic})

@main_bp.route('/demo_threat_intelligence', methods=['POST'])
def demo_threat_intelligence():
    # Simulate threat intelligence process
    ip_address = request.form.get('ip_address')
    # In a real scenario, you would perform actual threat analysis here
    threat_level = len(ip_address.split('.')) == 4
    return jsonify({"threat_level": "High" if threat_level else "Low"})
