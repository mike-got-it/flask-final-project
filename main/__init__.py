from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from main.config import config
# Making Flask Application
app = Flask(__name__)

# Object of Api class
api = Api(app)

# Application Configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mikemike212@localhost:3306/final_project'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'ThisIsHardestThing'
# app.config['JWT_SECRET_KEY'] = 'Dude!WhyShouldYouEncryptIt'
# app.config['JWT_BLACKLIST_ENABLED'] = True
# app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config.from_object(config)

# SqlAlchemy object
db = SQLAlchemy(app)

import main.models


# Generating tables before first request is fetched
@app.before_first_request
def create_tables():
    db.create_all()


# JwtManager object
jwt = JWTManager(app)


import main.resources

api.add_resource(resources.HealthCheck, '/health-status')
api.add_resource(resources.UserSignUp, '/sign-up')
api.add_resource(resources.UserSignIn, '/sign-in')
api.add_resource(resources.UserLogoutAccess, '/logout/access')

# if __name__ == '__main__':
#     app.run(port=8080, debug=True)
