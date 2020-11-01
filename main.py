# TODO: Plot addresses on map
# TODO: Change icon based on categories
# TODO: Create legend for categories
# TODO: Find way to open addresses in google maps

import folium
import pandas as pd
from geopy.geocoders import ArcGIS

def add_location_to_map(map, category, location, text):
    folium.Marker(
        location=location,
        icon=folium.Icon(icon=category, prefix='fa'),
        popup=text
    ).add_to(map)

def append_full_address_to_dataframe(locations_dataframe):
    locations_dataframe["Full Address"] = locations_dataframe.Address + ", " + locations_dataframe.City + ", " + locations_dataframe.State + " " + locations_dataframe.Zip.astype(str)
    return locations_dataframe

def create_base_map():
    raleigh_coords = [35.84, -78.65]
    map = folium.Map(location=raleigh_coords, zoom_start=12, tiles='openstreetmap')
    return map

def append_coordinates(locations_dataframe):
    coord = ArcGIS()
    locations_dataframe["Coordinates"] = locations_dataframe["Full Address"].apply(coord.geocode)
    locations_dataframe["Latitude"] = locations_dataframe.Coordinates.apply(lambda x: x.latitude)
    locations_dataframe["Longitude"] = locations_dataframe.Coordinates.apply(lambda x: x.longitude)
    return locations_dataframe

def read_location_list():
    locations_df = pd.read_csv("addresses.csv")
    return locations_df


def main():
    map = create_base_map()
    # Temporary variables to test add_location_to_map()
    category = "home"
    location = [35.84, -78.65]
    text = "North Hills"
    locations_dataframe = read_location_list()
    append_full_address_to_dataframe(locations_dataframe)
    append_coordinates(locations_dataframe)
    print(locations_dataframe)
    # add_location_to_map(map, category, location, text)
    # map.save("Map1.html")


main()
