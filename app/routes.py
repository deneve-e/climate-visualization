from flask import Blueprint, jsonify, render_template
from .models import ClimateData

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/data', methods=['GET'])
def get_data():
    data = ClimateData.query.all()
    # return jsonify([d.to_dict() for d in data])
    return render_template('data.html', data=data)
