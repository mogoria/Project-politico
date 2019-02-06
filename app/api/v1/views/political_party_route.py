""""defines implementation to routes for political parties"""
from flask import request
from app.api.v1.models.political_party_model import PoliticalParty
from . import v1_bp
from . import jsonify
from . import utils

Party = PoliticalParty()

@v1_bp.route('/political_parties', methods=['POST'])
def post_political_party():
    """route to create a political party"""
    new_political_party = dict()
    data = request.get_json(force=True)

    try:
        new_political_party = {
            'id' : data['id'],
            'name' : data['name'],
            'hqAddress' : data['hqAddress'],
            'logoUrl' : data['logoUrl']
            }

        if Party.get_party_by_id(new_political_party['id']):
            #party already exists
            return jsonify(utils.wrap_response(409, "Party already exists"))
        else:
            Party.create_party(**new_political_party)
            return jsonify(utils.wrap_response(201, new_political_party)), 201

    except KeyError:
        return jsonify(utils.wrap_response(400, "Please enter a valid request. " +
                                           "Fields include id, name, hqAddress and logoUrl")), 400

@v1_bp.route('/political_parties', methods=['GET'])
def get_all_political_parties():
    all_parties = Party.get_all_parties()

    if all_parties:
        return jsonify(utils.wrap_response(200,all_parties)), 200
    else:
        return jsonify(utils.wrap_response(404, "No data available"))