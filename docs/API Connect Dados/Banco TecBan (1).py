import sqlite3

banco = sqlite3.connect("Tecban.bd")

cursor = banco.cursor()

# 1. Criar tabelas (execute todas de uma vez)
# Cliente
cursor.execute("""CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_gmail VARCHAR(100),
    senha CHAR(11) UNIQUE,
    cpf VARCHAR(11) UNIQUE  
)""")

# Cliente Cadastro
cursor.execute("""CREATE TABLE IF NOT EXISTS Cadastro_Users(
               nome VARCHAR(100),
               email VARCHAR(100),
               senha CHAR(20) UNIQUE,
               cpf VARCHAR(11) UNIQUE
)""")


# Conta 
cursor.execute("""CREATE TABLE IF NOT EXISTS Conta (
    id_conta INTEGER PRIMARY KEY AUTOINCREMENT,
    saldo DECIMAL(10,2) DEFAULT 0,
    tipo VARCHAR(20),
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente)
)""")

