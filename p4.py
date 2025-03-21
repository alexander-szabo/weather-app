import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
df = pd.read_csv('weather.csv')

# Convert temperature to Fahrenheit
df['Ftemp'] = (df['Ktemp'] - 273.15) * (9/5) + 32

# Convert time to datetime and extract month and year
df['time'] = pd.to_datetime(df['time'])
df['month'] = df['time'].dt.month
df['year'] = df['time'].dt.year

# Group by month and year
avg_temps = df.groupby(['month', 'year'])['Ftemp'].mean().reset_index()

# Create a Streamlit app
st.title('Average Temperature by Month')

# Create a slider for the year
min_year = avg_temps['year'].min()
max_year = avg_temps['year'].max()
year = st.slider('Year', min_year, max_year, min_year)

# Filter data for the selected year
df_avg_year = avg_temps[avg_temps['year'] == year]

# Create a line plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_avg_year['month'], df_avg_year['Ftemp'], label=f'{year}')

# Set plot title and labels
ax.set_title('Average Temperature by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Temperature (F)')
ax.legend()

# Display the plot
st.pyplot(fig)
