# import the library
import folium
import pandas as pd


def getcodeCoordFromAddr(address):
    import googlemaps
    gmaps = googlemaps.Client('AIzaSyCNPwtdvyRqQrAUIxCUjSDVKXzy3eZj-NI')  # yay la sécurité

    res = gmaps.geocode(address)
    return res[0]



address = input('Addr : ')
info = getcodeCoordFromAddr(address)

print(info)

# Make a data frame with dots to show on the map
data = pd.DataFrame({
    'lat': [info['geometry']['location']['lat']],
    'lon': [info['geometry']['location']['lat']],
    'name': [info['address_components'][0]['long_name']],
    'value': [1]
})
data


# Make an empty map
m = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)

# I can add marker one by one on the map
for i in range(0, len(data)):
    folium.Circle(
        location=[data.iloc[i]['lon'], data.iloc[i]['lat']],
        popup=data.iloc[i]['name'],
        radius=data.iloc[i]['value'] * 10000,
        color='crimson',
        fill=True,
        fill_color='crimson'
    ).add_to(m)

# Save it as html
m.save('mymap.html')