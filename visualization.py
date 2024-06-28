import os
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_temperature_data(df, output_path='static/plot.png'):
    # Ensure the static directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='YEAR', y='TAVG', label="Average Temperature")
    sns.lineplot(data=df, x='YEAR', y='TMAX', label='Maximum Temperature')
    sns.lineplot(data=df, x='YEAR', y='TMIN', label='Maximum Temperature')
    plt.title('Temperature Changes Over Time')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.savefig(output_path)
    plt.close()