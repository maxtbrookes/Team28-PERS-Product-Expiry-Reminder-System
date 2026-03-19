from flask import request, jsonify
from datetime import datetime, timedelta
from app import app

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False

def calculate_expiry_date():
    return (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

@app.route('/calculate_expiry', methods=['POST'])
def calculate_expiry():
    data = request.get_json()
    expiry_date = data.get('expiryDate') if data else None

    if not expiry_date or not is_valid_date(expiry_date):
        estimated_date = calculate_expiry_date()
        return jsonify({
            "message": "Expiry date was missing or invalid. Estimated Date Provided.",
            "estimatedExpiryDate": estimated_date
        }), 200

    return jsonify({
        "message": "Expiry date provided.",
        "expiryDate": expiry_date
    }), 200