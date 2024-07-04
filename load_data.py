import pandas as pd
from app import db, app
from models import ClimateData

def load_csv_to_db(csv_file):
    df = pd.read_csv(csv_file)

    with app.app_context():
        db.create_all()
        for index, row in df.iterrows():
            data = ClimateData(
                station=row['STATION'],
                date=row['DATE'],
                latitude=row['LATITUDE'],
                longitude=row['LONGITUDE'],
                elevation=row['ELEVATION'],
                name=row['NAME'],
                tmax=row['TMAX'],
                tmin=row['TMIN']
            )
            db.session.add(data)
        db.session.commit()

if __name__ == '__main__':
    load_csv_to_db('data/JA000047662.csv')