from flask import Flask, render_template, request
import pandas as pd
from data_processing import load_and_process_data
from visualization import visualize_temperature_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    # Ensure the file is received from the request
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    file_path = f'data/{file.filename}'
    file.save(file_path)

    data = load_and_process_data(file_path)
    visualize_temperature_data(data)

    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)