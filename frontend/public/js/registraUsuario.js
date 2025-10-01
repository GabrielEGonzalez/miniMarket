let buttonResg = document.getElementById("registrar");


buttonResg.addEventListener("click",function(){
    let inputNombre = document.getElementById("nombre");
    let inputEmail = document.getElementById("email");
    let inputPass = document.getElementById("password");

    fetch("",{
        method:"POST",
        headers:"",
        body: JSON.stringify({
            nombre:inputNombre.value,
            email:inputEmail.value,
            password:inputPass.value,
            rol:"user"
        })
    }).then(res => res.json()).then().catch();
});