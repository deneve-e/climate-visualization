from flask import Blueprint, render_template, request, jsonify
from app import db
from app.models import Station, TemperatureRecord
from populate_database import populate_database_from_csv
from http_service import HttpService

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/stations/<int:station_id>', methods=['GET'])
def get_temperature_records_by_station_id(station_id):
        data = HttpService.fetch_data(station_id)
        
        return jsonify(data)
    
@bp.route('/api/stations', methods=['GET'])
def get_stations():
    stations = Station.query.all()
    stations_dict = [station.to_dict() for station in stations]
    print(stations_dict)
    return jsonify(stations_dict)

@bp.route('/data', methods=['GET'])
def check_data():
    stations = Station.query.all()
    temperature_records = TemperatureRecord.query.all()
    return render_template('data.html', stations=stations, temperature_records=temperature_records)

# Ensure to remove or secure these routes in a production environment to prevent accidental data loss.
@bp.route('/data/clean_tables', methods=['GET', 'POST'])
def clean_tables():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'cl34n t4bl3s':
            meta = db.metadata
            for table in reversed(meta.sorted_tables):
                print(f'Clearing table {table}')
                db.session.execute(table.delete())
            db.session.commit()
            return "Cleaned all data from all tables"
        else:
            return 'Wrong password!'
    return render_template('clean_tables.html')

@bp.route('/data/populate', methods=['GET'])
def populate_data():
    filesList = ['data/HR000142360.csv', 'data/JA000047662.csv', 'data/JA000047759.csv', 'data/JA000047765.csv', 'data/JAW00043302.csv', 'data/JAW00043323.csv', 'data/UPM00033345.csv', 'data/UPM00033837.csv']
    
    for f in filesList:
            populate_database_from_csv(f), 
    
    return 'Data populated successfully!'