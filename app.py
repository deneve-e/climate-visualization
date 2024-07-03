from flask import Flask, render_template, request
import pandas as pd
from data_processing import load_and_process_data
from visualization import visualize_temperature_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/', methods=['GET'])
def get_data():
    location = request.args.get('location')
    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')
    print(location, startDate, endDate)

    return f"{location}, from {startDate} to {endDate}"

if __name__ == '__main__':
    app.run(debug=True)