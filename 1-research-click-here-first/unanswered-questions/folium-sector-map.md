# Fixing KeyError: Couleur in a folium sector map

## Link to the original question

https://discuss.python.org/t/96052

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 with folium version 0.20.0 on a tiny made-up map file and no other person has rerun the test yet which means the page is unconfirmed. The real map file of the asker was not available.

## The question

On 19 June 2025 somebody asked on the Python help forum for the best method to build a folium map of all communes of one French department with four city sectors in four colours.
The map file has the properties nom and Secteur and Couleur and the style function and the tooltips failed with "KeyError: Couleur" and missing fields.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test file had two communes with all three properties and one commune with only a name.

- A style function that reads feature["properties"]["Couleur"] directly raised KeyError: Couleur which matches the report. One commune without the property is enough to stop the whole map.
- Filling in the missing properties for every commune before building the map worked: the map was built and all three colours and the tooltip text were present in the finished page.

## Best-guess answer

One possibility that fits the report is that the communes outside the four sectors have no Secteur and no Couleur in the map file.
The repair that worked in the test is a short loop before the map is built:

for f in data["features"]:
    p = f["properties"]
    p.setdefault("Secteur", "Hors secteur")
    p.setdefault("Couleur", "#cccccc")

folium.GeoJson(data,
    style_function=lambda f: {"fillColor": f["properties"]["Couleur"], "color": "black", "weight": 1, "fillOpacity": 0.6},
    tooltip=folium.GeoJsonTooltip(fields=["nom", "Secteur"], aliases=["Commune", "Secteur"])).add_to(m)

The loop gives every commune a sector label and a grey colour so the style function and the tooltip always find their fields.
The plain folium route needs no geopandas and no Fiona because folium reads the map file as an ordinary dictionary loaded with json.load.

The test file named folium_sectors.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
