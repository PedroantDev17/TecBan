

function botao() {

    let nome = document.getElementById("name").value
    let password = document.getElementById("senha").value
        fetch("http://127.0.0.1:5000/dados", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            mensagem: nome,
            senha: password
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