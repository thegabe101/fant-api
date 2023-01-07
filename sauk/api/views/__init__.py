
from api.views.mage_api import api as trip_reports_api

def mount_blueprints(app):
    app.register_blueprint(trip_reports_api)