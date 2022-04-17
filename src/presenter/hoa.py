from models.hoa import HOA
from typing import List
from repository import hoas


def get_hoas() -> List[HOA]:
    json_hoas = hoas.get_hoas()
    current_hoas = []
    for json_hoa in json_hoas:
        u = HOA(json_hoa.get("id"), json_hoa.get(
            "name"), json_hoa.get("address"))
        current_hoas.append(u)
    return current_hoas


def get_hoa(id):
    json_hoa = hoas.get_hoa(id)
    return json_hoa


def add_hoa(name, address):
    hoa_id = len(hoas.get_hoas()) + 1
    new_hoa = HOA(hoa_id, name, address)
    hoas.add_hoa(new_hoa)
