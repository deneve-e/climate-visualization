import matplotlib.pyplot as plt
import seaborn as sns

def visualize_temperature_data(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='YEAR', y='TAVG', label="Average Temperature")
    sns.lineplot(data=df, x='YEAR', y='TMAX', label='Maximum Temperature')
    sns.lineplot(data=df, x='YEAR', y='TMIN', label='Maximum Temperature')
    plt.title('Temperature Changes Over Time')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.snow()

visualize_temperature_data(annual_data)