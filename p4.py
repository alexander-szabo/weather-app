import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.widgets import Button, Slider
df = pd.read_csv('weather.csv')

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


df['Ftemp'] = (df['Ktemp'] - 273.15) * (9/5) + 32
df['time'] = pd.to_datetime(df['time'])
df['month'] = df['time'].dt.month
df['year'] = df['time'].dt.year

# Group by month and year
avg_temps = df.groupby(['month', 'year'])['Ftemp'].mean().reset_index()

# Set up figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.2)  # Make room for the slider

# Initial Plot for the First Year
min_year = avg_temps['year'].min()
first_year = avg_temps[avg_temps['year'] == min_year]
line, = ax.plot(first_year['month'], first_year['Ftemp'], label=f'{min_year}')

ax.set_title('Average Temperature by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Temperature (F)')
ax.legend()

# Slider Axis
ax_year = plt.axes([0.1, 0.05, 0.8, 0.03])  # Adjust position
year_slider = Slider(ax_year, 'Year', min_year, avg_temps['year'].max(), valinit=min_year, valstep=1)

# Update function for the slider
def update(val):
    year = int(year_slider.val)
    df_avg_year = avg_temps[avg_temps['year'] == year]
    
    # Update plot instead of redrawing it
    line.set_ydata(df_avg_year['Ftemp'])
    line.set_xdata(df_avg_year['month'])
    ax.relim()  # Recalculate limits
    ax.autoscale_view()  # Rescale view
    ax.legend([f'{year}'])  # Update legend
    
    fig.canvas.draw_idle()

year_slider.on_changed(update)

plt.show()