import requests
import random

def detect_deepfake(url):
    # This is a mock API call. In a real-world scenario, you would make an actual API request here.
    # For demonstration purposes, we'll return a random result.
    
    # Simulate API call delay
    import time
    time.sleep(2)
    
    result = random.choice([
        {"is_deepfake": True, "confidence": random.uniform(0.7, 0.99)},
        {"is_deepfake": False, "confidence": random.uniform(0.7, 0.99)}
    ])
    
    return result

def get_supported_platforms():
    return ["TikTok", "X", "Facebook", "Instagram", "Reddit", "Truth Social"]
