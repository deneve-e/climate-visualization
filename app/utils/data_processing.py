import pandas as pd

def load_and_process_data(file_path): 
    df = pd.read_csv(file_path)
    # Fill missing TAVG with the mean of TMAX and TMIN
    df['TAVG'] = df['TAVG'].fillna((df['TMAX'] + df['TMIN']) / 2)

    # Convert DATE column to datetime
    df['DATE'] = pd.to_datetime(df['DATE'])

    # Aggregate by year
    df['YEAR'] = df['DATE'].dt.year
    annual_data = df.groupby('YEAR').agg({'TAVG': 'mean', 'TMAX': 'mean', 'TMIN': 'mean'}).reset_index()

    # Inspect the first few rows
    print(df.head())

    return annual_data