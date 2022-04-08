
from crypt import methods
import mimetypes
from urllib import response
from flask import Flask, request
from flask_pymongo import PyMongo
from flask import render_template

from dotenv import load_dotenv

load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost/analisisyDiseñoAlgoritmos";
mongo = PyMongo(app)

@app.route("/user",methods=['POST'])
def create_user():
    
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if username and email and password:
        id = mongo.db.grafos.insert_one(
            {
                'username': username,
                'email': email,
                'password': password,
            }
        )
        response = {
            'id': str(id),
            'username': username,
            'email': email,
            'password': password
        }
        return response
    else:
        {'message': 'received'}

@app.route("/users",methods=['GET'])
def get_users():
    users = mongo.db.grafos.find()
    response = json_util.dumps(grafos)
    return Respose(response,mimetype='application/json')
if __name__ == '__main__':
    app.run()