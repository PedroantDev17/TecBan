cconst elemento = document.getElementById('meuElemento');

fetch("http://localhost:5000/dados", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        nome: "Paulo",
        idade: 20
    })
})
.then(res => res.json())
.then(data => console.log(data))