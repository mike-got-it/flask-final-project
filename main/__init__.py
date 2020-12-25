from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from flask_cors import CORS
from main.config import config
from main.utils.app_exception import AppException
from .db import init_db


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Application Configuration
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mikemike212@localhost:3306/final_project'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SECRET_KEY'] = 'ThisIsHardestThing'
    # app.config['JWT_SECRET_KEY'] = 'Dude!WhyShouldYouEncryptIt'
    # app.config['JWT_BLACKLIST_ENABLED'] = True
    # app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    app.config.from_object(config)

    @app.errorhandler(AppException)
    def handle_custom_exception(error):
        return jsonify(error.body), error.status_code

    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        return jsonify(message=e.description), e.code

    db.init_app(app)
    with app.app_context():
        init_db()
    return app

# import main.resources
#
# api.add_resource(resources.HealthCheck, '/health-status')
# api.add_resource(resources.UserSignUp, '/sign-up')
# api.add_resource(resources.UserSignIn, '/sign-in')
# api.add_resource(resources.UserLogoutAccess, '/logout/access')

# if __name__ == '__main__':
#     app.run(port=8080, debug=True)
