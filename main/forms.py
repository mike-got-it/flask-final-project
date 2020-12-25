from marshmallow import fields, Schema, validate, ValidationError, validates

from main.models import User, Category


class SignInFormSchema(Schema):
    username = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)


class SignUpFormSchema(Schema):

    username = fields.Str(required=True, allow_none=False, validate=validate.Length(min=6, max=30))
    password = fields.Str(required=True, allow_none=False, validate=validate.Length(min=8))

    @validates('username')
    def validate_unique_username(self, username):
        if User.find_by_username(username):
            raise ValidationError(f'Username {username} has already been taken.')


class ItemSchema(Schema):

    name = fields.Str(required=True, allow_none=False, validate=validate.Length(min=1, max=120))
    description = fields.Str(required=True, allow_none=False, validate=validate.Length(min=1, max=2000))
    category_id = fields.Integer(required=False)

    @validates('category_id')
    def validate_category_exist(self, category_id):
        if not Category.find_by_id(category_id):
            raise ValidationError('Category not found')


# user = {'username': 'aaaaaa', 'password': 'asdaasdasd'}
#
# schema = SignUpFormSchema()
#
#
# print(schema.validate(user))

