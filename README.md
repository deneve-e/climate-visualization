# Climate Change Visualization

## Overview

This project visualizes historical climate data to show changes in temperature over time. Users can enter a location and use a range input to interactively explore how the climate has changed during specific years. The application uses preset CSV data for historical climate data.

## Setup

1. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open a browser and go to `http://127.0.0.1:5000`.

3. Enter a location and adjust the range input to explore how the climate has changed over time. The application will process the historical data and display the visualization.

## File Structure

- `app.py`: Main application file
- `data_processing.py`: Contains functions for loading and processing data
- `visualization.py`: Contains functions for visualizing data
- `templates/`: Contains HTML templates
    - `index.html`: Main page for user input
    - `data.html`: Page to display the visualization
- `static/`: Contains static files like the generated plot
- `data/`: Directory for preset CSV files with historical climate data
- `.venv/`: Virtual environment directory
- `requirements.txt`: File listing all dependencies
- `README.md`: Project description and setup guide

## Preset CSV Data

The preset CSV files for historical climate data should be placed in the `data/` directory. Each file should contain columns such as `STATION`, `NAME`, `DATE`, `TAVG`, `TMAX`, and `TMIN`.

## Example CSV Format

"STATION","NAME","DATE","TAVG","TMAX","TMIN"

"JA000047420","NEMURO, JA","1931-01-01",,"-6.7","-10.2"

"JA000047420","NEMURO, JA","1931-01-02",,"-2.2","-12.6"

"JA000047420","NEMURO, JA","1931-01-03",,"-0.8","-3.8"

"JA000047420","NEMURO, JA","1931-01-04",,"-0.7","-7.1"

"JA000047420","NEMURO, JA","1931-01-05",,"-0.3","-9.6"

## ~Contributions~

~Contributions are welcome! Please fork the repository and submit a pull request.~

## ~License~

~This project is licensed under the MIT License.~
