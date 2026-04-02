from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/dados", methods=["POST"])
def dados():

    info = request.json

    print(info)

    return "Recebido"

@app.route("/senha", methods=["POST"])
def senha():

    senha= request.json

    print(senha)

app.run(debug=True)

