import json
from models.hoa import HOA


def get_hoas():
    f = open(
        "./data/hoas.json")
    data = json.load(f)
    return data


def get_hoa(id):
    f = open(
        "./data/hoas.json")
    data = json.load(f)
    for hoa in data:
        if id == hoa["id"]:
            return hoa


def add_hoa(hoa: HOA):
    f = open(
        "./data/hoas.json")
    data = json.load(f)
    f.close()
    hoa_json = json.loads(json.dumps(hoa))
    data.append(hoa_json)
    with open("./data/hoas.json", 'w') as f:
        json.dump(data, f)
