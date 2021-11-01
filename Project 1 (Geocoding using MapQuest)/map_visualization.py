from folium.map import Icon, Popup
import pandas as pd
import folium
from folium.plugins import MarkerCluster

m = folium.Map(location=[12.8730640, 80.221902], tiles='OpenStreetMap', zoom_start = 7)
 
MarkerCluster = MarkerCluster().add_to(m)
data = pd.read_csv('geodata.csv')
# print(data.head())

for i,row in data.iterrows():
    lat = data.at[i,'lat']
    lng = data.at[i,'lng']
    clg_name = data.at[i,'Name']
    
    popup = data.at[i, 'Name'] + '<br>' + str(data.at[i,'State']) + '<br>' + str(data.at[i,'Country'])
    # print(popup)
    folium.Marker(location=[lat,lng], popup=popup , icon=folium.Icon(color='green')).add_to(MarkerCluster)
    
m.save('output.html')