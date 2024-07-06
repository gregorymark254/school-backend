from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from auth.models import User
from extensions import db
from auth.schemas import UserSchema

api = Blueprint('auth', __name__)


@api.post('/register')
def register():
    if not request.is_json:
        return {"error": "Missing JSON in request"}, 400

    schema = UserSchema()
    user = schema.load(request.json)
    db.session.add(user)
    db.session.commit()

    return {"message": f"User {user.email} Registered successfully"}, 201


@api.post('/login')
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return {"error": "Invalid email or password"}, 400

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity={'id': user.id, 'role': user.role.value})
        user_data = {
            'firstname': user.first_name,
            'role': user.role.value,
        }
        return {"access_token": access_token, "user": user_data}, 200
    else:
        return {'error': 'Incorrect email or password'}, 401
