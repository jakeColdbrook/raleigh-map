# TODO: Create list of addresses
# TODO: Separate addresses into meaningful categories
# TODO: Read addresses into Python
# TODO: Plot addresses on map
# TODO: Create legend for categories
# TODO: Find way to open addresses in google maps

import folium


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


def main():
    map = create_base_map()
    # Temporary variables to test add_location_to_map()
    category = "home"
    location = [35.84, -78.65]
    text = "North Hills"

    add_location_to_map(map, category,location,text)
    map.save("Map1.html")


main()
