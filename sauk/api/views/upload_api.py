from flask import Blueprint, current_app, request, jsonify
import logging


api = Blueprint("upload_api", __name__)
log = logging.getLogger('werkzeug')

@api.route('/api/2/bard/upload', methods=['POST'])
def bard():
    log.info("dfad")
    return "adfa"
