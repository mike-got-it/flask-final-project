from marshmallow import fields, Schema, validate, ValidationError

from models import User


# def validate_unique_username(username):
#     if User.find_by_username(username):
#         raise ValidationError("Username" + username + "has already been taken.")


class SignInFormSchema(Schema):
    username = fields.Str(required=True, allow_none=False, )
    password = fields.Str(required=True, allow_none=False, )


class SignUpFormSchema(Schema):
    username = fields.Str(required=True, allow_none=False, validate=validate.Length(min=1, max=50))
    password = fields.Str(required=True, allow_none=False, validate=validate.Length(min=8))


# user = {'username': 'aaaaaa', 'password': 'asdaasdasd'}
#
# schema = SignUpFormSchema()
#
#
# print(schema.validate(user))

