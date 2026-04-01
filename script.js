function botao() {

    let nome = document.getElementById("name").value
    let password = document.getElementById("senha").value
    fetch("https://pedroantdev17.github.io/TecBan/")
        fetch('http://127.0.0.1:5000/', {
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
