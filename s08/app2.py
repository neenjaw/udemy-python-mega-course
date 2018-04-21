import folium

map = folium.Map(location=[52.133333,-106.683333], zoom_start=6, tiles="Mapbox Bright")

group = folium.FeatureGroup(name="My Map")

coordinate_group = [
    {
        "location": [52.133333, -106.683333],
        "popup": "Hi, This is Saskatoon",
        "icon_color": "green"
    },
    {
        "location": [54, -104],
        "popup": "Hi, This is nowhere",
        "icon_color": "red"
    }
]


for coordinates in coordinate_group:
    group.add_child(folium.Marker(location=coordinates["location"], popup=coordinates["popup"], icon=folium.Icon(color=coordinates["icon_color"])))

map.add_child(group)

map.save("Map1.html")