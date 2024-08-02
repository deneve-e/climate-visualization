from app.models import TemperatureRecord, Station

class HttpService:
    def fetch_data(station_id):
        records = TemperatureRecord.query.filter_by(station_id=station_id).all()
        # Process and return data
        return [record.to_dict() for record in records]