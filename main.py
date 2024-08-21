
from flask import Flask, render_template, request, jsonify
import folium

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (37.7749, -122.4194)
    map = folium.Map(location=start_coords, zoom_start=12, tiles='OpenStreetMap')

    # Add draw functionality
    folium.plugins.Draw(export=True).add_to(map)

    # Save the map
    map.save('templates/map.html')
    return render_template('index.html')

@app.route('/get_area_info', methods=['POST'])
def get_area_info():
    area_coords = request.json.get('coords')
    # Dummy data for example
    info = {
        "Area": f"Coordinates: {area_coords}",
        "Population": "10,000",
        "Average Income": "$50,000",
        "Other Info": "Details about the area."
    }
    return jsonify(info)

if __name__ == "__main__":
    app.run(debug=True)
