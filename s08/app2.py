import folium
import pandas
import json

def get_color_for_elevation(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 3000:
        return "orange"
    else:
        return "red"

volcano_data = pandas.read_csv("volcanoes.csv")

# coordinate_list = volcano_data.T.to_dict().values()
coordinate_list = volcano_data.to_dict('records')

map = folium.Map(location=[47.609722, -122.333056], zoom_start=3, tiles="Mapbox Bright")

vgroup = folium.FeatureGroup(name="Volcanoes")
pgroup = folium.FeatureGroup(name="Population")

pgroup.add_child(folium.GeoJson(
    data=(open('world.json', 'r', encoding="utf-8-sig").read()),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

for coordinate in coordinate_list:

    location_coords = [coordinate["Latitude (dd)"],coordinate["Longitude (dd)"]]

    location_elements = """<span class="volcano-name">{0}</span>,
                          <span class="country">{1}</span>,
                          <span class="elevation">Elevation: {2}m</span>"""

    location_elements = location_elements.format(coordinate["Volcano Name"], coordinate["Country"], coordinate["Elevation (m)"])

    location_html = folium.Html(location_elements, script=True)
    location_popup = folium.Popup(html=location_html, parse_html=True)

    location_color = get_color_for_elevation(coordinate["Elevation (m)"])

    vgroup.add_child(folium.CircleMarker(location=location_coords, popup=location_popup, radius=6, fill=True, fill_color=location_color, fill_opacity=0.7, color="grey"))


map.add_child(vgroup)
map.add_child(pgroup)
map.add_child(folium.LayerControl())

map.save("Map1.html")