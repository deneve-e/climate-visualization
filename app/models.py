from . import db

class station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_code = db.Column(db.String(50), unique=True, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    elevation = db.Column(db.Float)
    name = db.Column(db.String(50))

class TemperaturRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    tmax = db.Column(db.Float)
    tmin = db.Column(db.Float)