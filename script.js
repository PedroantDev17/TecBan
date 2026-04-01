function botao() {

    let nome = document.getElementById("name").value
    let password = document.getElementById("senha").value

    fetch("http://localhost:5000/dados", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            mensagem: nome, 
            senha: password
        })
    })

}