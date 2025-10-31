let productos = [];
let contendor = document.getElementById("contenedor");
let search = document.querySelector("#busqueda");
let filterPrecio = document.getElementById("precio");

fetch("http://127.0.0.1:8000/producto/").then(res => res.json()).then(data => {
  //console.log("Datos del backend:", data); 
  productos = data;
  mostrarDatos(productos);
}).catch(e => console.error(e))


search.addEventListener("input", function (e) {
  let texto = e.target.value.toLowerCase();
  let filtroProducto = productos.filter(prod =>
    prod.nombre.toLowerCase().includes(texto)
  )
  mostrarDatos(filtroProducto);
});

filterPrecio.addEventListener("change", function () {

  let valor = filterPrecio.value;
  let listaPrecio;
  if (valor === "todos") {
        listaPrecio = productos;
    } else {
    let fill = filterPrecio.value.split('-');
    console.log(fill);
    listaPrecio = productos.filter(prod => {
      if (fill[0] <= prod.precio && fill[1] >= prod.precio) {
        return prod
      }
    })
    }
    console.log(listaPrecio);
    mostrarDatos(listaPrecio);
  
});

function mostrarDatos(filtroProducto) {
  contendor.innerHTML = "";
  filtroProducto.forEach(producto => {
    let html = `
      <div class="head-card">
        <div class="body-card">
          <img src="https://images.unsplash.com/photo-1626675431647-2dbf75028ec6?auto=format&fit=crop&q=80&w=400" alt="Imagen de producto" />
          <h2>${producto.nombre}</h2>
          <p>${producto.descripcion}</p>
          <div class="footer-card">
            <h2>$${producto.precio}</h2>
            <button>Agregar al carrito</button>
          </div>
        </div>
      </div>
    `;
    contendor.innerHTML += html;
  });
}