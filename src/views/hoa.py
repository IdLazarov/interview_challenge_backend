from flask import Blueprint
from flask import jsonify, make_response, request
from presenter.hoa import get_hoas, add_hoa, get_hoa
import json

hoa_views = Blueprint("hoa", __name__)


@hoa_views.route('/hoas', methods=['GET'])
def get_all_hoas():
    hoas = get_hoas()
    r = []
    for hoa in hoas:
        r.append(hoa.__dict__)
    return make_response(jsonify({"hoas": r}), 200)


@hoa_views.route('/hoa/<int:id>', methods=['GET'])
def get_hoa_by_id(id):
    hoa = get_hoa(id)
    return make_response(jsonify({"hoa": hoa}), 200)


@hoa_views.route('/hoa', methods=['POST'])
def add_hoa_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if "name" not in data and "address" not in data:
        return make_response(jsonify({"status": "bad request"}), 400)

    name = data["name"]
    address = data["address"]

    add_hoa(name, address)

    return make_response(jsonify({"status": "success"}), 200)
