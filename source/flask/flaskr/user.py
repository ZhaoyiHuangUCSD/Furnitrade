from flaskr.db import get_db
import pymongo
from bson.json_util import dumps
import json

########### Additional Dependencies Please Add Here ###################
#from flask_httpauth import HTTPBasicAuth
from flaskr import auth
from flaskr.db import get_users_collection

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
    jsonify
)
from flask_restful import Api, Resource, url_for
from bson import ObjectId

bp = Blueprint('user', __name__, url_prefix='/user')
api = Api(bp);


# take an id of user, delete from database
class Delete(Resource):
    def get(self, username):
        users = get_users_collection();
        users.remove({'username': username});
        pass;


# This updates/edits the user's Profile
# First verify if new modification is valid;
# Then update databse fields if so.
# Output: boolean - if success; msg - error message
# Due by Sat; Mao Li
class Edit(Resource):
    @auth.login_required
    def post(self):
        # Step1: Get post's jason file
        posted_data = request.get_json();
        new_username = posted_data['username'];
        new_email = posted_data['email'];
        new_address = posted_data['address'];

        # Step2: Verify edited username and email

        # 2.1 get user's original info from database
        # TODO: get user without getting all collection
        user_id = session['user_id'];
        users = auth.get_users_collection();
        user = users.find_one({'_id': ObjectId(user_id)});

        # 2.2 verify the changes to user's Profile
        if new_username != user['username']:
            if auth.user_exist(new_username, users):
                return jsonify({
                    "status": 310,
                    "msg": 'New username already exists'
                })
            if not auth.check_username_valid(new_username):
                return jsonify({
                    "status": 310,
                    "msg": "New username contains invalid symbols"
                })

        if new_email != user['email']:
            if not auth.check_email_valid(new_email):
                return jsonify({
                    "status": 318,
                    "msg": 'New email invalid',
                })
            if auth.email_exist(new_email, users):
                return jsonify({
                    "status": 318,
                    "msg": 'New email already exists'
                })

        # Step 3: update the user's info in database
        users.update_one({'_id': ObjectId(user_id)},
                          {"$set": {"username": new_username, "email": new_email, "address": new_address}});

        return jsonify({
            "status": 200,
            "msg": "Update/Edit succeeded"
        })


# take an id return user info
# Get all user related info in database as JSON file.
class Profile(Resource):
    @auth.login_required
    def get(self, username):
        # Get user profile from database
        #user_id = session['user_id'];
        users = get_users_collection();

        if users.find_one({"username": username}) is None:
            return jsonify({
                "status": 312,
                "msg": "User doesn't exist"
                })

        user = users.find_one({'username': username});
        current_username = user['username'];
        current_email = user['email'];
        current_address = user['address'];
        # current_picture = user['picture'];

        # Collect profile data
        retJson = {
            "status": 200,
            "msg": 'Get profile succeeded',
            'username': current_username,
            'email': current_email,
            'address': current_address,
            #'picture': current_picture
        }

        # Return received data
        return jsonify(retJson);



api.add_resource(Delete, '/delete/<string:username>');
api.add_resource(Edit, '/edit');
api.add_resource(Profile, '/profile/<string:username>');
