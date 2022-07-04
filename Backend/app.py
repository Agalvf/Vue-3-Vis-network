from distutils.debug import DEBUG
from pickle import TRUE
from flask import Flask, jsonify, request
from flask_cors import CORS


DEBUG = TRUE

app = Flask(__name__)
app.config.from_object(__name__)

#Habilitar los CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/karger_mincut', methods=['GET', 'POST'])
def ping_pong():
    import karger_mincut
    return karger_mincut.iniciar_grafo(request.json) 


if __name__ == '__main__':
    app.run()