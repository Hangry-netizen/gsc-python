from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from gsc_api.blueprints.gscs.views import gscs_api_blueprint
from gsc_api.blueprints.approvals.views import approvals_api_blueprint
from gsc_api.blueprints.single_communities.views import single_communities_api_blueprint

app.register_blueprint(gscs_api_blueprint, url_prefix='/api/v1/gscs')
app.register_blueprint(approvals_api_blueprint, url_prefix='/api/v1/approvals')
app.register_blueprint(single_communities_api_blueprint, url_prefix='/api/v1/single-communities')
