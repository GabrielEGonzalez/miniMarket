let contendor = document.getElementById("contenedor");

window.onload = function () {
    fetch("http://127.0.0.1:8000/producto/").then(res => res.json()).then(data => {
        
        data.forEach(producto => {
            let div = document.createElement("div");
            let h2 = document.createElement("h2");
            let p = document.createElement("p");
            let div2 = document.createElement("div");
            let img = document.createElement("img");
            let div3 = document.createElement("div");
            let button = document.createElement("button");
            let h2precio = document.createElement("h2");
            //img.src = 'https://cdn.iconscout.com/icon/premium/png-256-thumb/producto-terminado-icon-svg-download-png-8634015.png?f=webp';
            img.src = 'https://images.unsplash.com/photo-1626675431647-2dbf75028ec6?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1033';//`https://ui-avatars.com/api/?name=${producto.nombre}&size=200`;


            div.classList.add("head-card");
            div2.classList.add("body-card");
            div3.classList.add("footer-card");

            button.textContent = "Add to Cart"
            button.dataset.id = producto.id
            h2.textContent = producto.nombre;
            p.textContent= producto.descripcion;
            h2precio.textContent = "$"+ producto.precio;

            button.addEventListener("click",function(){
                let id_prod = this.dataset.id;
                let secret = getCookie("secret_key");
                let id_user;
                if (secret) {
                    let [id,email,rol] = secret.split("&");
                    id_user = id;
                }
                fetch("http://127.0.0.1:8000/Carrito/add/producto",{
                    method: "",
                    headers: {"Content-Type":"application/json"},
                    body: JSON.stringify({
                        usuario_id: id_user,
                        producto_id: id_prod
                    })
                }).then(
                    res => res.json()
                ).then(
                    resp => {
                        if(resp){
                        
                        }
                    }
                ).catch(
                    err = console.error("error:",error)
                )
            });

            div3.appendChild(h2precio);
            div3.appendChild(button);
            div2.appendChild(img)
            div2.appendChild(h2);
            div2.appendChild(p)
            div2.appendChild(div3);
            div.appendChild(div2);
            contendor.appendChild(div);
        });
        //console.log(data);
    }).catch(error => {

        console.error('Error al obtener los datos:', error);
    });
};