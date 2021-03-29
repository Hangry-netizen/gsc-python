from flask import Blueprint, jsonify, request
from models.approval import *

approvals_api_blueprint = Blueprint('approvals_api',
                             __name__)

@approvals_api_blueprint.route('/', methods=['GET'])
def index():
  approvals = Approval.select()
  return jsonify([{
      "id": approval.id,
      "gsc_name": approval.gsc_name,
      "ff_email": approval.ff_email
      }
      for approval in approvals
    ])
    
@approvals_api_blueprint.route('/', methods=['POST'])
def create():
    data = request.json

    gsc_name = data.get('gsc_name')
    ff_email = data.get('ff_email')

    if gsc_name and ff_email:
      approval = Approval(
        gsc_name = gsc_name,
        ff_email = ff_email
      )
      if approval.save():
        return jsonify({
            "message": "Successfully added gsc name",
            "status": "success",
            "approval": {
                "id": approval.id,
                "gsc_name": approval.gsc_name,
                "ff_email": approval.ff_email
            }
        })
      else:
        return jsonify({
            "message": "All fields are required!",
            "status": "failed"
        })