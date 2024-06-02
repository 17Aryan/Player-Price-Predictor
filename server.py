from flask import  Flask ,request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager,jwt_required
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import os

app=Flask(__name__)
app.config['SECRET_KEY']='JWTSECRETKEY'

bcrypt=Bcrypt(app)
jwt=JWTManager(app)

#connection with database
client=MongoClient("mongodb+srv://admin:admin@atlascluster.soa8zni.mongodb.net/")
db=client['login_signup']
user_collection=db['Users']

@app.route('/')
def home():
    return "Server Running!", 200

@app.route('/signup', methods=['POST'])
def signup():
    data=request.json
    username=data.get('username')
    password=data.get('password')
    email=data.get('email')
    name=data.get('name')
    hashed_password = bcrypt.generate_password_hash(password).decode('utf8')
    user=user_collection.find_one({"username":username})

    if user or user_collection.find_one({"email":email}):
        return jsonify({"message":"User already exists"}), 400
    # new_user=user_collection.insert_one({"username":username, "password":  hashed_password})
    # response=user_collection.find_one({"_id":new_user.inserted_id})
    # response.pop("_id")
    # return jsonify(response), 201
    else:
        user_collection.insert_one({'username':username, 'password':hashed_password,'email':email,'name':name})
        return jsonify({'message':'user created successfully'}),201
    
@app.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    username_or_email=data.get('username')
    password=data.get('password')

    user=user_collection.find_one({"$or":[{'username':username_or_email},{'email':username_or_email}]})

    if user and bcrypt.check_password_hash(user['password'],password):
        return jsonify({'message':'Login successful'}),200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/usercheckout',methods=['GET'])
def usercheckout():
    data=request.get_json()
    username=data.get('username')
    # print(username)
    user=user_collection.find_one({"username":username})
    # print(user)
    if user:
        return jsonify({"message":"False"}),400
    else:
        return jsonify({"message":"True"}),201
@app.route('/user', methods=['GET'])
def user():
    # Return the first name and last name of the user
    data = request.json
    username = data.get('username')
    user = user_collection.find_one({'username': username})
    return jsonify({'firstName': user['firstName'], 'lastName': user['lastName']}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=1000)
