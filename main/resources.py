from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt
)
import pdb
from marshmallow import ValidationError
import main.forms as forms
from main.models import User, RevokedToken


class HealthCheck(Resource):
    def get(self):
        return 'ok'


class UserSignUp(Resource):

    def post(self):
        data = request.json
        try:
            forms.SignUpFormSchema().load(data)
        except ValidationError as err:
            return {"message": str(err)}, 400

        username = data['username']
        password = data['password']
        new_user = User(username=username, password=User.generate_hash(password))

        try:
            new_user.save_to_db()
            return {
                "message": f'User {username} has been created'
            }
        except:
            return {'message': 'Something went wrong'}, 500


class UserSignIn(Resource):

    def post(self):
        data = request.json
        try:
            forms.SignInFormSchema().validate(data)
        except ValidationError as err:
            return {"message": str(err)}, 400

        username = data['username']
        password = data['password']

        # searching user by username
        current_user = User.find_by_username(username)

        # user doesn't exist
        if not current_user:
            return {'message': "Wrong credentials"}, 401

        # user exists, comparing password and hash
        if User.verify_hash(password, current_user.password):
            # generating access token and refresh token
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return {
                'message': f'Logged in as {username}',
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': "Wrong credentials"}, 401


class UserLogoutAccess(Resource):

    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']

        try:
            # Revoking access token
            revoked_token = RevokedToken(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500
