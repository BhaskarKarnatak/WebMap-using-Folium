import pandas as pd
import folium
colour=['purple', 'darkblue', 'lightred', 'lightblue', 'blue', 'lightgrayblack', 'darkpurple', 'darkgreen',
        'pink', 'beige', 'darkred', 'gray', 'green', 'red', 'orange']
data=pd.read_csv("NationalPark.csv")

mape=folium.Map(location=[22.2458,79.0882],zoom_start=4.5,max_zoom=6,min_zoom=4,tiles="OpenStreetMap")

for i in range(14):
    mape.add_child(folium.Marker(location=[data["Latitude"][i],data["Longitude"][i]],
                                 popup=data["Name"][i],icon=folium.Icon(color=colour[i],
                                                                        icon_color='white', icon='paw', angle=0, prefix='fa')))
mape.save("National Park Map.html")