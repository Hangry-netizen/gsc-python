from flask import Blueprint, jsonify, request
from models.report import Report

reports_api_blueprint = Blueprint('reports_api',
                             __name__)

@reports_api_blueprint.route('/', methods=['GET'])
def index():
    reports = Report.select()
    return jsonify([{
        "concerns": report.concerns,
        "actions": report.actions
    } for report in reports])
    
@reports_api_blueprint.route('/', methods=['POST'])
def create():
    data = request.json

    gsc = data.get('gsc')
    concerns = data.get('concerns')
    actions = data.get('actions')

    report = Report(
            gsc = gsc,
            concerns = concerns,
            actions = actions,
        )
    if report.save():
        return jsonify({
            "message": "Report successfully submitted.",
            "status": "success",
            "report": {
            "conerns": report.concerns,
            "actions": report.actions
            }
        })
    elif report.errors != 0:
        return jsonify({
            "message": [error for error in report.errors],
            "status": "failed"
        })

