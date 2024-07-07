from app import db

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