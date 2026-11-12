# Rebuilds the KeyError from a sector map in folium and tests a repair (Python forum topic 96052)
import json, folium
print("folium", folium.__version__)
def square(x, y): return {"type": "Polygon", "coordinates": [[[x, y], [x + 0.05, y], [x + 0.05, y + 0.05], [x, y + 0.05], [x, y]]]}
features = [
    {"type": "Feature", "geometry": square(7.25, 43.70), "properties": {"nom": "Nice", "Secteur": "Nice", "Couleur": "#e41a1c"}},
    {"type": "Feature", "geometry": square(7.10, 43.58), "properties": {"nom": "Antibes", "Secteur": "Antibes", "Couleur": "#377eb8"}},
    {"type": "Feature", "geometry": square(7.00, 43.80), "properties": {"nom": "Village sans secteur"}},          # no Secteur and no Couleur
]
geo = {"type": "FeatureCollection", "features": features}

def build(data, style):
    m = folium.Map(location=[43.7, 7.2], zoom_start=10)
    folium.GeoJson(data, style_function=style, tooltip=folium.GeoJsonTooltip(fields=["nom", "Secteur"], aliases=["Commune", "Secteur"])).add_to(m)
    return m.get_root().render()

try:
    build(geo, lambda f: {"fillColor": f["properties"]["Couleur"], "color": "black", "weight": 1, "fillOpacity": 0.6})
    print("posted style: no error")
except Exception as e: print("direct lookup f['properties']['Couleur'] ->", type(e).__name__ + ":", e)
try:
    build(geo, lambda f: {"fillColor": f["properties"].get("Couleur", "#cccccc")})
    print(".get() in the style only: no error")
except Exception as e: print(".get() in the style only ->", type(e).__name__ + ":", str(e)[:110])

# repair: give every commune all three fields before building the map
fixed = json.loads(json.dumps(geo))
for f in fixed["features"]:
    p = f["properties"]; p.setdefault("Secteur", "Hors secteur"); p.setdefault("Couleur", "#cccccc")
html = build(fixed, lambda f: {"fillColor": f["properties"]["Couleur"], "color": "black", "weight": 1, "fillOpacity": 0.6})
print("after filling in the missing fields: map built,", len(html), "characters of HTML | all three colours present:", all(c in html for c in ("#e41a1c", "#377eb8", "#cccccc")), "| tooltip fields present:", "Hors secteur" in html)
