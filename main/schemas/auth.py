from marshmallow import Schema, fields, validates, ValidationError, validate


class SignInFormSchema(Schema):
    username = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)


class SignUpFormSchema(Schema):

    username = fields.Str(required=True, allow_none=False, validate=validate.Length(min=6, max=30))
    password = fields.Str(required=True, allow_none=False, validate=validate.Length(min=8))

    # @validates('username')
    # def validate_unique_username(self, username):
    #     if User.find_by_username(username):
    #         raise ValidationError(f'Username {username} has already been taken.')
