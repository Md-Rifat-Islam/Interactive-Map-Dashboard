
from flask import Flask, send_from_directory
import folium
from folium.plugins import Draw
import os

app = Flask(__name__)

# Ensure the static directory exists
os.makedirs('static', exist_ok=True)

# Generate the map and save it as an HTML file
#@app.before_first_request
def generate_map():
    center_location = [24.3961, 88.6041]
    m = folium.Map(location=center_location, zoom_start=15,
                   tiles="CartoDB Positron",  # High-contrast map
                   attr="© <a href='https://carto.com/attributions'>CARTO</a>, © OpenStreetMap contributors")

    # Add a Draw control to the map
    draw = Draw(export=True)
    draw.add_to(m)

    # Save the initial map as an HTML file
    map_file = "static/map.html"
    m.save(map_file)

@app.route('/')
def index():
    return send_from_directory('static', 'map.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
