import nasapy
import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inline # to display plots

#get data and load into dataframe
fireball = nasapy.fireballs(date_min='2010-01-01', date_max='2025-10-31', return_df=True)


#clean up and process data
#remove duplicate records
fireball.dropna(inplace=True)

#convert data points to float data type
fireball['lat'] = fireball['lat'].astype(float)
fireball['lon'] = fireball['lon'].astype(float)
fireball['energy'] = fireball['energy'].astype(float)

#check first 5 records
#print(fireball.head())


#plot the data using folium map object
m = folium.Map(zoom_start=4)

for i in range(0, len(fireball)):
    folium.Circle(
        location=[fireball.iloc[i]['lat'], fireball.iloc[i]['lon']],
        tooltip=f"Date: {fireball.iloc[i]['date']}\nLatitude/Longitude: {fireball.iloc[i]['lat']}, {fireball.iloc[i]['lon']}",
        radius=fireball.iloc[i]['energy'] * 20,
        color='black',
        fill=True,
        fill_color='red'
    ).add_to(m)

m.save('fireball_map.html')
m


#investigating further because i am nosy and high density areas ( bigger circles)

#extract date from datetime column and sort ascending by energy value
fireball['datetime'] = fireball['date']
fireball['date'] = fireball['datetime'].apply(lambda x: x.split(' ')[0])

fireball.sort_values(by='energy', ascending=False, inplace=True)

#plot fireball energy values by date
plt.figure(figsize=(16, 6))
energy_plot = sns.barplot(x='date', y='energy', data=fireball[0:20])
energy_plot.set_title('Top 20 Fireball Energy Values by Date', fontsize=16)
energy_plot = energy_plot.set_xticklabels(fireball['date'], rotation=45, fontsize=10)
plt.show()














