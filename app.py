# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# from config import Config
# from load_data import populate_database_from_csv

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/data', methods=['GET'])
# def get_data():
#     stations = Station.query.all()
#     temperature_records = TemperatureRecord.query.all()
#     return render_template('data.html', stations=stations, temperature_records=temperature_records)

# # Ensure to remove or secure these routes in a production environment to prevent accidental data loss.
# @app.route('/data/clean_tables', methods=['GET', 'POST'])
# def clean_tables():
#     if request.method == 'POST':
#         password = request.form.get('password')
#         if password == 'cl34n t4bl3s':
#             meta = db.metadata
#             for table in reversed(meta.sorted_tables):
#                 print(f'Clearing table {table}')
#                 db.session.execute(table.delete())
#             db.session.commit()
#             return "Cleaned all data from all tables"
#         else:
#             return 'Wrong password!'
#     return render_template('clean_tables.html')

# @app.route('/data/populate', methods=['GET'])
# def populate_data():
#     populate_database_from_csv()
#     return 'Data populated successfully!'

# if __name__ == '__main__':
#     app.run(debug=True)