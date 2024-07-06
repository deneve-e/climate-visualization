from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_code = db.Column(db.String(50), unique=True, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    elevation = db.Column(db.Float)
    name = db.Column(db.String(50))
    temperature_records = db.relationship('TemperatureRecord', backref='station', lazy=True)

class TemperatureRecord(db.Model):
    __tablename__ = 'temperature_records'
    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    tmax = db.Column(db.Float)
    tmin = db.Column(db.Float)
    
    __table_args__ = (
        db.UniqueConstraint('station_id', 'date', name='_station_date_uc'),
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    stations = Station.query.all()
    temperature_records = TemperatureRecord.query.all()
    return render_template('data.html', stations=stations, temperature_records=temperature_records)

# Ensure to remove or secure these routes in a production environment to prevent accidental data loss.
@app.route('/clean_tables')
def clean_tables():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f'Clearing table {table}')
        db.session.execute(table.delete())
    db.session.commit()
    return "Cleaned all data from all tables"

if __name__ == '__main__':
    app.run(debug=True)