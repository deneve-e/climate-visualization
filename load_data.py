import csv
from datetime import datetime
from app import app, db, Station, TemperatureRecord

def populate_database_from_csv(csv_file):
    with app.app_context():
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            stations_seen = set() # To track stations already added
            
            for row in reader:
                station_code = row['STATION']
                if station_code not in stations_seen:
                    # Add station if not already added
                    station = Station(
                        station_code=station_code,
                        latitude=float(row['LATITUDE']),
                        longitude=float(row['LONGITUDE']),
                        elevation=float(row['ELEVATION']),
                        name=row['NAME']
                    )
                db.session.add(station)
                stations_seen.add(station_code)
                db.session.commit() # Commit here to ensure station IDs are available
        
            # Add temperature record
            station = Station.query.filter_by(station_code=station_code).first()
            date_str = row['DATE']
            date = datetime.strptime(date_str, '%Y-%m') # Assuming DATE format is 'YYYY-MM'
                
            temperature_record = TemperatureRecord(
                station_id=station.id,
                date=date,
                tmax=float(row['TMAX']) if row['TMAX'].strip() else None,
                tmin=float(row['TMIN']) if row['TMIN'].strip() else None,
            )
            db.session.add(temperature_record)
        
        db.session.commit()

if __name__ == '__main__':
    populate_database_from_csv('data/JA000047662.csv')