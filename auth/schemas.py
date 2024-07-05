from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String
from extensions import ma
from auth.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    email = String(required=True, validate=validate.Email())
    password = String(required=True, validate=validate.Length(min=8))

    @validates_schema
    def validate_email(self, data, **kwargs):
        email = data.get("email")

        if User.query.filter_by(email=email).count():
            raise ValidationError({'error': f'Email {email} already registered'})

    class Meta:
        model = User
        load_instance = True
        exclude = ["_password"]
