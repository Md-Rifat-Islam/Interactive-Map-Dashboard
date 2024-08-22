import folium
from folium.plugins import Draw

# Set the default center location (Rajshahi coordinates)
center_location = [24.3961, 88.6041]

# Create the map with a high-contrast tile
m = folium.Map(location=center_location, zoom_start=15,
               tiles="CartoDB Positron",  # High-contrast map
               attr="© <a href='https://carto.com/attributions'>CARTO</a>, © OpenStreetMap contributors")

# Add a Draw control to the map
draw = Draw(export=True)
draw.add_to(m)

# Save the initial map as an HTML file
map_file = "map.html"
m.save(map_file)

print(f"Initial map saved as {map_file}")
