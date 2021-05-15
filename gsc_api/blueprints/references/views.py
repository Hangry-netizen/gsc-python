from flask import Blueprint, jsonify, request
from models.reference import Reference

references_api_blueprint = Blueprint('references_api',
                             __name__)

@references_api_blueprint.route('/', methods=['GET'])
def index():
    references = Reference.select()
    return jsonify([{
        "referral_name": reference.referral_name,
        "reasons_gscf_makes_a_good_partner": reference.reasons_gscf_makes_a_good_partner,
        "good_match_for_gscf": reference.good_match_for_gscf
    } for reference in references])
    
@references_api_blueprint.route('/', methods=['POST'])
def create():
    data = request.json

    gsc = data.get('gsc')
    referral_name = data.get('referral_name')
    reasons_gscf_makes_a_good_partner = data.get('reasons_gscf_makes_a_good_partner')
    good_match_for_gscf =data.get('good_match_for_gscf')

    reference = Reference(
            gsc = gsc,
            referral_name = referral_name,
            reasons_gscf_makes_a_good_partner = reasons_gscf_makes_a_good_partner,
            good_match_for_gscf = good_match_for_gscf
        )
    if reference.save():
        return jsonify({
            "message": "Reference successfully submitted. Thank you!",
            "status": "success",
            "reference": {
            "referral_name": reference.referral_name,
            "reasons_gscf_makes_a_good_partner": reference.reasons_gscf_makes_a_good_partner,
            "good_match_for_gscf": reference.good_match_for_gscf
            }
        })
    elif reference.errors != 0:
        return jsonify({
            "message": [error for error in reference.errors],
            "status": "failed"
        })

