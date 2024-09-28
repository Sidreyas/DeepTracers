from flask import Blueprint, jsonify, request
from models import db, Contact

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/solutions')
def solutions():
    solutions = [
        {"name": "KYC Security", "description": "Enhance your Know Your Customer (KYC) processes with AI-powered identity verification and fraud detection."},
        {"name": "Media Verification", "description": "Detect and prevent the spread of manipulated media, including deepfakes and altered images."},
        {"name": "Threat Intelligence", "description": "Stay ahead of potential threats with our advanced AI-driven threat intelligence platform."}
    ]
    return jsonify(solutions)

@main_bp.route('/api/use-cases')
def use_cases():
    use_cases = [
        {"name": "Law Enforcement", "description": "Empower law enforcement agencies with advanced AI tools for digital investigations and threat assessment."},
        {"name": "Cybersecurity", "description": "Protect your organization's digital assets with AI-powered threat detection and response."},
        {"name": "KYC", "description": "Streamline and secure your Know Your Customer processes with AI-driven verification."},
        {"name": "Digital Forensics", "description": "Leverage AI to enhance digital forensics investigations and evidence analysis."}
    ]
    return jsonify(use_cases)

@main_bp.route('/api/resources')
def resources():
    resources = {
        "blog_posts": [
            {"title": "The Future of AI in Cybersecurity", "date": "May 15, 2023"},
            {"title": "5 Ways AI is Revolutionizing Threat Detection", "date": "April 28, 2023"},
            {"title": "Understanding Deepfakes and Their Impact on Security", "date": "April 10, 2023"}
        ],
        "whitepapers": [
            {"title": "AI-Powered Threat Intelligence: A Comprehensive Guide"},
            {"title": "The Role of Machine Learning in Modern Cybersecurity"}
        ],
        "video_tutorials": [
            {"title": "Getting Started with AI Threat Detection", "duration": "15:30"},
            {"title": "Advanced Techniques in AI-Driven Forensics", "duration": "22:45"}
        ]
    }
    return jsonify(resources)

@main_bp.route('/api/technology')
def technology():
    technology = {
        "ai_ml": {
            "title": "AI and Machine Learning",
            "description": "Our platform leverages cutting-edge AI and machine learning algorithms to provide advanced threat detection capabilities.",
            "features": ["Deep learning neural networks", "Natural language processing", "Computer vision algorithms"]
        },
        "big_data": {
            "title": "Big Data Analytics",
            "description": "Process and analyze vast amounts of data in real-time to identify patterns and potential threats.",
            "features": ["Distributed computing", "Stream processing", "Advanced data visualization"]
        },
        "continuous_learning": {
            "title": "Continuous Learning",
            "description": "Our AI models continuously improve and adapt to new threats through ongoing training and feedback loops.",
            "features": ["Automated model retraining", "Active learning techniques", "Human-in-the-loop validation"]
        },
        "scalable_infrastructure": {
            "title": "Scalable Infrastructure",
            "description": "Our cloud-native architecture ensures high availability and scalability to meet the demands of organizations of all sizes.",
            "features": ["Containerized microservices", "Auto-scaling capabilities", "Multi-region deployment"]
        }
    }
    return jsonify(technology)

@main_bp.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    new_contact = Contact(name=data['name'], email=data['email'], message=data['message'])
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({"message": "Your message has been sent successfully!"}), 201
