import json
import requests

BASE_URL = "https://www.nottingham.ac.uk/estates/documents/accessplans/{}{}a.pdf"
NOT_FOUND = 404
SUCCESS = 200

with open("buildings.json") as f:
    campuses = json.load(f)

floor_plans = {campus: {building: {} for building in buildings} for campus, buildings in campuses.items()}

for campus, buildings in campuses.items():
    for building_name, building_code in buildings.items():
        for i in range(97, 123):
            floor_name = chr(i)
            url = BASE_URL.format(building_code, floor_name)
            r = requests.get(url)
            if r.status_code == SUCCESS:
                print(f"{campus}: Added floor plan to '{building_name}': {floor_name}: {url}")
                floor_plans[campus][building_name][floor_name] = url
            else:
                break

with open("pdfs.json", "w") as f:
    json.dump(floor_plans, f, indent=4)
