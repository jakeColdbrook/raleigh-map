# TODO: Convert addresses to latitude and longitude
# TODO: Plot addresses on map
# TODO: Change icon based on categories
# TODO: Create legend for categories
# TODO: Find way to open addresses in google maps

import folium
import pandas as pd


def create_base_map():
    raleigh_coords = [35.84, -78.65]
    map = folium.Map(location=raleigh_coords, zoom_start=12, tiles='openstreetmap')
    return map


def add_location_to_map(map, category, location, text):
    folium.Marker(
        location=location,
        icon=folium.Icon(icon=category, prefix='fa'),
        popup=text
    ).add_to(map)


def read_location_list():
    location_df = pd.read_csv("addresses.csv")
    return location_df


def main():
    map = create_base_map()
    # Temporary variables to test add_location_to_map()
    category = "home"
    location = [35.84, -78.65]
    text = "North Hills"
    location_dataframe = read_location_list()

    add_location_to_map(map, category, location, text)
    map.save("Map1.html")


main()
