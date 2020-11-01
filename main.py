# TODO: Find way to deploy so that it is viewable by whole family

import folium
import pandas as pd
from geopy.geocoders import ArcGIS


def add_location_to_map(map, category, latitude, longitude, text):
    folium.Marker(
        location=[latitude, longitude],
        icon=folium.Icon(icon=get_icon(category), prefix='fa'),
        popup=text
    ).add_to(map)
    marker.bindTooltip("text here", {permanent: true, offset: [0, 12]});


def append_full_address_to_dataframe(locations_dataframe):
    locations_dataframe[
        "Full Address"] = locations_dataframe.Address + ", " + locations_dataframe.City + ", " + locations_dataframe.State + " " + locations_dataframe.Zip.astype(
        str)
    return locations_dataframe


def append_coordinates(locations_dataframe):
    coord = ArcGIS()
    locations_dataframe["Coordinates"] = locations_dataframe["Full Address"].apply(coord.geocode)
    locations_dataframe["Latitude"] = locations_dataframe.Coordinates.apply(lambda x: x.latitude)
    locations_dataframe["Longitude"] = locations_dataframe.Coordinates.apply(lambda x: x.longitude)
    return locations_dataframe


def create_base_map():
    raleigh_coords = [35.84, -78.65]
    map = folium.Map(location=raleigh_coords, zoom_start=12, tiles='openstreetmap')
    return map


def create_zip_for_iteration(locations_dataframe):
    category = list(locations_dataframe["Category"])
    latitude = list(locations_dataframe["Latitude"])
    longitude = list(locations_dataframe["Longitude"])
    text = list(locations_dataframe["Text"])
    zipped_location_info = zip(category, latitude, longitude, text)
    return zipped_location_info


def get_icon(category):
    if category == "New Construction":
        icon = "home"
    if category == "Landmark":
        icon = "thumb-tack"
    if category == "Company":
        icon = "building"
    return icon


def read_location_list():
    locations_df = pd.read_csv("addresses.csv")
    return locations_df


def main():
    map = create_base_map()

    # # Temporary variables to test add_location_to_map()
    # category = "home"
    # location = [35.84, -78.65]
    # text = "North Hills"
    locations_dataframe = read_location_list()
    append_full_address_to_dataframe(locations_dataframe)
    append_coordinates(locations_dataframe)
    zipped_location_info = create_zip_for_iteration(locations_dataframe)

    for category, latitude, longitude, text in zipped_location_info:
        add_location_to_map(map, category, latitude, longitude, text)
    map.save("Map1.html")


main()
