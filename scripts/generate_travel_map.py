"""A simple script for reading in a file of information on locations and creating a folium plot"""

import folium
import pandas as pd


def add_marker(
    map: folium.Map,
    mouseover: str,
    label: str,
    latitude: float,
    longitude: float,
    icon: str = "info-sign",
    color: str = "blue",
):
    """
    Function to add an icon to a map
    """
    icon = folium.Icon(
        icon=icon,
        color=color,
    )

    folium.Marker(
        location=[latitude, longitude],
        tooltip=mouseover,
        popup=label,
        icon=icon,
    ).add_to(map)


def main():

    # create initial travel map at a reasonable initial location and zoom
    travel_map = folium.Map(
        location=(30, -30),
        zoom_start=2,
    )

    # read in file with information needed to plot locations
    input_filepath = "assets/folium/travel_map_data.csv"
    df = pd.read_csv(input_filepath)

    # adding markers one by one to map object
    for index, row in df.iterrows():
        add_marker(
            map=travel_map,
            mouseover=row["mouseover"],
            label=row["label"],
            latitude=row["lat"],
            longitude=row["long"],
            icon=row["icon"],
            color=row["color"],
        )

    # saving output to assets
    output_path = "assets/folium/travel_map.html"
    print(f"Writing output map to {output_path}")
    travel_map.save(output_path)


if __name__ == "__main__":
    main()
