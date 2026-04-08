from flask import Flask, request
from flask_cors import CORS
import sqlite3

banco = sqlite3.connect("Tecban.bd", check_same_thread=False)
cursor = banco.cursor()



app = Flask(__name__)
CORS(app)

# Rota Dados
@app.route("/dados", methods = ["POST"])
def login():
    info = request.json

    username = info["mensagem"]
    senha = info["senha"]
    cpf = info["cpf"]

    print(info)

    cursor.execute("""INSERT INTO Cliente (nome_gmail, senha, cpf) 
                   VALUES (?, ?, ?)""", 
                   (username, senha, cpf))
    banco.commit()

    return "Recebido"
    

# Rota senha
@app.route("/senha", methods = ["POST"])
def atualizar_senha():
    info = request.json

    password_esqueci = info['esqueci_senha']

    print(info)

    # cursor.execute("""UPDATE Cliente 
    #                SET senha = (?) 
    #                WHERE nome_gmail = (?)""", 
    #                (password_esqueci,))
    banco.commit()

    return "Recebido"

# Rota cadastro
@app.route("/cadastro", methods = ["POST"])
def cadastro():
    info = request.json

    nome = info['name']
    email = info['email']
    senha = info['senha']
    cpf = info['cpf']
    

    print(info)

    cursor.execute("""INSERT INTO Cadastro_Users (nome, email, senha, cpf) 
                   VALUES (?, ?, ?, ?)""", 
                   (nome, email, senha, cpf))
    banco.commit()

    return "Informações Recebidas"


if __name__ == "__main__":
    app.run(debug=True)
    banco.close()