

let inputlogin = document.getElementById("login");
let urlDestino = "http://127.0.0.1:5500/frontend/index.html"; 

inputlogin.addEventListener("click",function(){
    let inputEmail = document.getElementById("email");
    let inputPass = document.getElementById("password");
    fetch("http://127.0.0.1:8000/user/login",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        credentials:"include",
        body:JSON.stringify({
            email:inputEmail.value,
            password:inputPass.value 
        })
    }).then().then(resp=>{
        console.log(resp);
        window.location.href = urlDestino; 
    }).catch(error => console.log(error));
});