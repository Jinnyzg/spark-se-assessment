from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from project.server import bcrypt, db
from project.server.models import User

user_blueprint = Blueprint('users', __name__)

class UserIndexAPI(MethodView):
    def get(self):
        users = db.session.query(User)
        reponseInfo = []
        for user in users:
            reponseInfo.append(user.email)
        return make_response(jsonify(reponseInfo)), 201


# define the API resources
userIndex_view = UserIndexAPI.as_view('userIndex_api')

# add Rules for API Endpoints
user_blueprint.add_url_rule(
    '/users/index',
    view_func=userIndex_view,
    methods=['GET']
)