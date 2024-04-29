import json
import re
from datetime import datetime

#Function to parse the data from the Adidas json format to Strava json format
def json_parser(file):
    f = open(file)
    data = json.load(f)

    if "subjective_feeling" in data:
        description = data["subjective_feeling"]
        name = description + " run from " + str(datetime.fromtimestamp(data["start_time"] / 1000))
    else:
        description = ""
        name = "Run from " + str(datetime.fromtimestamp(data["start_time"] / 1000))

    if "dehydration_volume" in data:
        dehydration = data["dehydration_volume"]
    else:
        dehydration = ''

    type = "Run"
    sport_type = "Run"
    start_date_local = datetime.fromtimestamp(data["start_time"] / 1000).isoformat() + 'Z'
    elapsed_time = data["duration"] / 1000
    distance = 1000
    calories = data["calories"]
    total_elevation_gain = 0
    max_speed = 3
    map_polyline = None  # Initialize with None if not found

    # Find features with specific types to extract details
    for feature in data["features"]:
        if feature["type"] == "track_metrics":
            distance = feature["attributes"]["distance"]
            total_elevation_gain = feature["attributes"]["elevation_gain"]
            max_speed = feature["attributes"]["max_speed"]  # Added line to extract max_speed
        elif feature["type"] == "map":
            map_polyline = feature["attributes"]["encoded_trace"]

    # You can further process the date (activity_date) if needed

    json_data = {
        "name": name,
        "type": type,
        "sport_type": sport_type,
        "start_date_local": start_date_local,
        "elapsed_time": elapsed_time,
        "distance": distance,
        "calories": calories,
        "description": description,
        "dehydration": dehydration,
        "total_elevation_gain": total_elevation_gain,
        "max_speed": max_speed,
        "map_polyline": map_polyline
    }

    # Convert to JSON string
    json_string = json.dumps(json_data, indent=4)

    # Print or use the JSON string as needed
    return json_data
