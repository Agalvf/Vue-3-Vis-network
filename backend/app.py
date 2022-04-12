from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from bson import json_util, ObjectId

load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(__name__)
app.config['MONGO_URI'] = "mongodb://localhost/analisisyDiseñoAlgoritmos";

CORS(app,resources={r"/*":{'origins':"*"}})
mongo = PyMongo(app)

@app.route("/shark",methods=["GET"])
def shark():
    return("Shark 🦈!")

""" @app.route("/user",methods=['POST'])
def create_grafos():
    
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
        return not_found()

@app.route("/user",methods=['GET'])
def get_grafos():
    grafos = mongo.db.grafos.find()
    response = json_util.dumps(grafos)
    return Response(response,mimetype='application/json')

@app.route("/user/<id>",methods=["GET"])
def get_users(id):
    grafo = mongo.db.grafos.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(grafo)
    return Response(response, mimetype="application/json") """

@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Resource Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run()