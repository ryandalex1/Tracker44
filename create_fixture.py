import csv
import json

expansions = []
with open('expansions.csv', newline='') as file:
    reader = csv.reader(file)
    pk = 1
    for row in reader:
        scenario = {
            "model": "scenarios.expansion",
            "pk": pk,
            "fields": {
                "name": row[0],
                "abbreviation": row[1],
            }
        }
        expansions.append(scenario)
        pk += 1

sub_expansions = []
with open('sub_expansions.csv', newline='') as file:
    reader = csv.reader(file)
    pk = 1
    for row in reader:
        scenario = {
            "model": "scenarios.sub_expansion",
            "pk": pk,
            "fields": {
                "name": row[0],
                "abbreviation": row[1],
                "parent": [row[2]]
            }
        }
        expansions.append(scenario)
        pk += 1

scenarios = []
with open('scenarios.csv', newline='') as file:
    reader = csv.reader(file)
    pk = 1
    for row in reader:
        scenario = {
            "model": "scenarios.scenario",
            "pk": pk,
            "fields": {
                "name": row[0],
                "expansion": [row[1]],
                "sub_expansion": [row[2]],
                "number": row[3],
                "board": row[4],
                "scenario_type": row[5]
            }
        }
        scenarios.append(scenario)
        pk += 1

with open("complete_fixture.json", "w") as outfile:
    json.dump(expansions + sub_expansions + scenarios, outfile)
