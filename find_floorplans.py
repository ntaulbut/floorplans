import json
import requests

BASE_URL = "https://www.nottingham.ac.uk/estates/documents/accessplans/{}{}a.pdf"
SUCCESS = 200
A_ORD = 97
Z_ORD = 123
LOWER_GROUND_FLOOR = "lg"


def alpha_range():
    for n in range(A_ORD, Z_ORD + 1):
        yield chr(n)


with open("buildings.json") as f:
    campuses = json.load(f)

floor_plans = {
    campus: {building: {} for building in buildings}
    for campus, buildings in campuses.items()
}

for campus, buildings in campuses.items():
    for building_name, building_code in buildings.items():
        r = requests.get(BASE_URL.format(building_code, LOWER_GROUND_FLOOR))
        if r.status_code == SUCCESS:
            print(
                f"{campus}: Added lower ground floor plan to '{building_name}': {r.url}"
            )
            floor_plans[campus][building_name][LOWER_GROUND_FLOOR] = r.url

        for floor_name in alpha_range():
            r = requests.get(BASE_URL.format(building_code, floor_name))
            if r.status_code == SUCCESS:
                print(
                    f"{campus}: Added floor plan to '{building_name}': {floor_name}: {r.url}"
                )
                floor_plans[campus][building_name][floor_name] = r.url
            else:
                break

with open("pdfs.json", "w") as f:
    json.dump(floor_plans, f, indent=2)
