import pandas as pd

#Load the CSV data
file_path = "data/3729265.csv"
df = pd.read_csv(file_path)

# Inspect the first few rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Fill missing TAVG with the mean of TMAX and TMIN
df['TAVG'] = df['TAVG'].fillna((df['TMAX'] + df['TMIN']) / 2)

# Convert DATE column to datetime
df['DATE'] = pd.to_datetime(df['DATE'])

# Aggregate by year
df['YEAR'] = df['DATE'].dt.year
annual_data = df.groupby('YEAR').agg({'TAVG': 'mean', 'TMAX': 'mean', 'TMIN': 'mean'}).reset_index()

# Inspect the first few rows
print(df.head())