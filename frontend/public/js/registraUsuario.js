let buttonResg = document.getElementById("registrar");
let urlDestino = "http://127.0.0.1:5500/frontend/index.html"; 

buttonResg.addEventListener("click",function(){
    let inputNombre = document.getElementById("nombre");
    let inputEmail = document.getElementById("email");
    let inputPass = document.getElementById("password");

    fetch("http://127.0.0.1:8000/user/register",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        credentials: "include",
        body: JSON.stringify({
            nombre:inputNombre.value,
            email:inputEmail.value,
            password:inputPass.value,
            rol:"user"
        })
    }).then(res => res.json())
    .then(resp =>{console.log(resp);
        window.location.href = urlDestino; 
    })
    .catch(error => console.log(error));
});