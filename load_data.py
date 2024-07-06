import csv
from datetime import datetime
from app import app, db, Station, TemperatureRecord

def populate_database_from_csv(csv_file):
    with app.app_context():
        try:
            with open(csv_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
            
                for row in reader:
                    station_code = row['STATION']
                    existing_station = Station.query.filter_by(station_code=station_code).first()
                    if existing_station:
                        print(f"Station with code {station_code} already exists. Skipping...")
                        continue

                    # Add station if not already added
                    station = Station(
                        station_code=station_code,
                        latitude=float(row['LATITUDE']),
                        longitude=float(row['LONGITUDE']),
                        elevation=float(row['ELEVATION']),
                        name=row['NAME']
                    )
                    db.session.add(station)
                    db.session.commit() # Commit here to ensure station IDs are available
                    station_id = station.id
                    print(f"Added station: {station_code}, ID: {station_id}")
                                
# TODO: finish adding temperature records
                    # Add temperature record
                    date_str = row['DATE']
                    try:
                        date = datetime.strptime(date_str, '%Y-%m')
                    except ValueError as e:
                         print(f"Error parsing date '{date_str}': {e}")
                         continue
                     
                    tmax=float(row['TMAX']) if row['TMAX'].strip() else None
                    tmin=float(row['TMIN']) if row['TMIN'].strip() else None
        
                    temperature_record = TemperatureRecord(
                        station_id=station_id,
                        date=date,
                        tmax=tmax,
                        tmin=tmin
                    )
                    
                    db.session.add(temperature_record)
                    db.session.commit()
                    print(f"Added temperature record: {date}, Tmax: {tmax}, Tmin: {tmin}")
        except Exception as ex:
            print(f"Error processing CSV file: {ex}")    

if __name__ == '__main__':
    populate_database_from_csv('data/JA000047662.csv')