function login() {

    let login = document.getElementById("login").value
    let password = document.getElementById("senha").value
    let cpf = document.getElementById("cpf").value
        fetch("http://127.0.0.1:5000/dados", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "mensagem": login,
            "senha": password,
            "cpf": cpf
        })
    })
    
};

function senha() {

    let senha = document.getElementById("esqueci_senha").value
        fetch("http://127.0.0.1:5000/senha", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "esqueci_senha": senha
        })
    })
    
};

function cadastro() {

    let nome = document.getElementById("name").value
    let email = document.getElementById("email").value
    let senha = document.getElementById("senha").value
    let cpf = document.getElementById("cpf").value
        fetch("http://127.0.0.1:5000/cadastro", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "name": nome,
            'email': email,
            "senha": senha,
            "cpf": cpf
        })
    })
    
};