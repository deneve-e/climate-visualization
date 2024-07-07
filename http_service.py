from app.models import TemperatureRecord, Station

class HttpService:
    def fetch_data(location, start_date, end_date):
        records = TemperatureRecord.query.filter(TemperatureRecord.date.between(start_date, end_date), Station.name == location).all()
        # Process and return data
        return [record.to_dict() for record in records]