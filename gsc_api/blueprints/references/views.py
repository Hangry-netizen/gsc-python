from flask import Blueprint, jsonify, request
from models.reference import Reference

references_api_blueprint = Blueprint('references_api',
                             __name__)

@references_api_blueprint.route('/', methods=['GET'])
def index():
    references = Reference.select()
    return jsonify([{
        "ref_name": reference.ref_name,
        "ref_email": reference.ref_email,
        "reasons_gscf_makes_a_good_partner": reference.reasons_gscf_makes_a_good_partner,
        "good_match_for_gscf": reference.good_match_for_gscf,
        "is_approved": reference.is_approved
    } for reference in references])
    
@references_api_blueprint.route('/', methods=['POST'])
def create():
    data = request.json

    gsc = data.get('gsc')
    ref_name = data.get('ref_name')
    ref_email = data.get('ref_email')
    reasons_gscf_makes_a_good_partner = data.get('reasons_gscf_makes_a_good_partner')
    good_match_for_gscf = data.get('good_match_for_gscf')

    reference = Reference(
            gsc = gsc,
            ref_name = ref_name,
            ref_email = ref_email,
            reasons_gscf_makes_a_good_partner = reasons_gscf_makes_a_good_partner,
            good_match_for_gscf = good_match_for_gscf
        )
    if reference.save():
        return jsonify({
            "message": "Reference has been submitted successfully.",
            "status": "success",
            "reference": {
            "ref_name": reference.ref_name,
            "ref_email": reference.ref_email,
            "reasons_gscf_makes_a_good_partner": reference.reasons_gscf_makes_a_good_partner,
            "good_match_for_gscf": reference.good_match_for_gscf,
            "is_approved": reference.is_approved
            }
        })
    elif reference.errors != 0:
        return jsonify({
            "message": [error for error in reference.errors],
            "status": "failed"
        })

