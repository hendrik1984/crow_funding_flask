from flask import Blueprint, request
from app import db
from models.user import User
from utils.json_response import render_json

user_bp = Blueprint('user_bp', __name__)

# Create User
@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password_hash=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return render_json("User created successfully", 201, "success", {"id": new_user.id, "username": new_user.username, "email": new_user.email})

# Get All Users
@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    if users is None:
        return render_json("Users not found", 404, "success", None)
        
    return render_json("Retrieved list of users", 200, "success", [{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

# Get Single User
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return render_json("Users not found", 404, "success", None)
    
    return render_json("Retrieved one user", 200, "success", {'id': user.id, 'username': user.username, 'email': user.email})

# Update User
@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return render_json("Users not found", 404, "success", None)

    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password_hash = data.get('password', user.password_hash)
    db.session.commit()
    return render_json("Updated one user", 200, "success", {'id': user.id, 'username': user.username, 'email': user.email})

# Delete User
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return render_json("Users not found", 404, "success", None)
    
    db.session.delete(user)
    db.session.commit()
    return render_json("Delete one user", 200, "success", None)
