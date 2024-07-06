import csv
from datetime import datetime
from app import app, db, Station, TemperatureRecord

def populate_database_from_csv(csv_file):
    with app.app_context():
        try:
            with open(csv_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
            
                first_row = next(reader)
                station_code = first_row['STATION']
                existing_station = Station.query.filter_by(station_code=station_code).first()
                if not existing_station:
                    # Add station if not already added
                    station = Station(
                        station_code=station_code,
                        latitude=float(first_row['LATITUDE']),
                        longitude=float(first_row['LONGITUDE']),
                        elevation=float(first_row['ELEVATION']),
                        name=first_row['NAME']
                    )
                    db.session.add(station)
                    db.session.commit() # Commit here to ensure station IDs are available
                    station_id = station.id
                    print(f"Added station: {station_code}, ID: {station_id}")
                else:
                    station_id = existing_station.id
                    print(f"Station with code {station_code} already exists. Using existing ID: {station_id}")
                     
                # Reset file pointer to re-read rows for temperature records
                file.seek(0)
                reader = csv.DictReader(file)
                
                temperature_records = []
                     
                for row in reader:
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
                    
                    temperature_records.append(temperature_record)
                    print(f"Added temperature record: {date}, Tmax: {tmax}, Tmin: {tmin}")

                db.session.add_all(temperature_records)
                db.session.commit()

        except Exception as ex:
            print(f"Error processing CSV file: {ex}")    

if __name__ == '__main__':
    filesList = ['data/HR000142360.csv', 'data/JA000047662.csv', 'data/JA000047759.csv', 'data/JA000047765.csv', 'data/JAW00043302.csv', 'data/JAW00043323.csv', 'data/UPM00033345.csv', 'data/UPM00033837.csv']
    
    
    for f in filesList:
            populate_database_from_csv(f), 