from . import db

class ClimateData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(20))
    date = db.Column(db.String(10))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    elevation = db.Column(db.Float)
    name = db.Column(db.String(50))
    tmax = db.Column(db.Float)
    tmin = db.Column(db.Float)

    def to_dict(self):
        return {
            'station': self.station,
            'date': self.date,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'elevation': self.elevation,
            'name': self.name,
            'tmax': self.tmax,
            'tmin': self.tmin
        }