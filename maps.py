import folium
from geopy.geocoders import Nominatim
import database as db
from pprint import pprint

geocode_test = '555 Showers Dr, Mountain View, CA 94040'

entry_coords = db.get_coordinates_and_info()

g = Nominatim(user_agent="geo")

# testing geocoding library
loc = g.geocode(geocode_test)
print(loc.latitude, loc.longitude)
print(entry_coords)
print(entry_coords[0][0])
m = folium.Map(location=[loc.latitude, loc.longitude], zoom_start=10)

folium.Marker([loc.latitude, loc.longitude], popup="Geocode Test").add_to(m)

# plot entries from database
for log_entry in entry_coords:
    folium.Marker([log_entry[0], log_entry[1]], popup=f"{log_entry[3]} {log_entry[2]}").add_to(m)

m.save("map.html")
