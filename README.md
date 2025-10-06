
---

# 🛍️ Urban Market – Mini Marketplace de Ropa de Segunda Mano

**Urban Market** es un mini marketplace web donde los usuarios pueden **comprar y vender ropa de segunda mano o nueva**, fomentando la **moda sostenible** y el **consumo consciente**.
Este proyecto fue desarrollado con el objetivo de practicar **FastAPI (backend)** y **frontend con HTML, CSS y JavaScript**.

---

## 🚀 **Objetivo del proyecto**

Crear una aplicación web funcional que simule un pequeño marketplace con las siguientes características:

* Registro y autenticación de usuarios.
* Gestión de productos (nuevo o usado).
* Carrito de compras con suma total.
* Búsqueda y filtrado de productos.

El enfoque principal fue aplicar buenas prácticas en **desarrollo backend con FastAPI** y conectar el frontend mediante peticiones **Fetch API**.

---

## 🧠 **Tecnologías utilizadas**

### 🔹 Backend

* **FastAPI** – Framework principal para la API.
* **SQLite** – Base de datos ligera para desarrollo local.
* **Pydantic** – Validación de datos.
* **Uvicorn** – Servidor ASGI para ejecutar la app.

### 🔹 Frontend

* **HTML5** – Estructura de las páginas.
* **CSS3** – Estilos, diseño responsivo y animaciones suaves.
* **JavaScript (Fetch API)** – Conexión con el backend y manejo del carrito.

---

## ⚙️ **Características principales**

✅ Registro e inicio de sesión de usuarios
✅ Listado de productos con filtros (nuevo / usado)
✅ Agregar productos al carrito
✅ Cálculo del total de compra
✅ Diseño limpio, responsivo y funcional
✅ Backend completo con API REST construida en FastAPI

---

## 🔑 **Rutas principales (API)**

| Método | Ruta            | Descripción                 |
| ------ | --------------- | --------------------------- |
| `POST` | `/register`     | Registrar un nuevo usuario  |
| `POST` | `/login`        | Iniciar sesión              |
| `GET`  | `/products`     | Obtener todos los productos |
| `POST` | `/products/add` | Agregar un nuevo producto   |
| `GET`  | `/cart`         | Ver productos en el carrito |
| `POST` | `/cart/add`     | Agregar producto al carrito |

---

## 🧭 **Guía rápida de uso**

1. Clona este repositorio

   ```bash
   git clone https://github.com/GabrielEGonzalez/urban-market.git
   cd urban-market/backend
   ```

2. Instala las dependencias

   ```bash
   pip install fastapi uvicorn pydantic
   ```

3. Ejecuta el servidor

   ```bash
   uvicorn main:app --reload
   ```

4. Abre el frontend

   * Desde la carpeta `/frontend`, abre `index.html` en el navegador.

5. Listo 🎉
   Ya puedes explorar el marketplace, registrarte, iniciar sesión y probar todas las funciones.

---


## 🧩 **Próximas mejoras**

* Sistema de autenticación con **JWT Tokens**.
* Dashboard para vendedores.
* Integración de **Stripe / PayPal**.
* Panel de administración.
* Modo oscuro y diseño más moderno.

---

## 🌿 **Propósito del proyecto**

Urban Market nace con la idea de combinar **tecnología y sostenibilidad**.
Cada prenda vendida o reutilizada ayuda a reducir el desperdicio textil y fomenta la **moda circular**.

> “Viste con estilo, cuida el planeta.” 🌎

---

## 👨‍💻 **Autor**

**Desarrollado por:** [Gabriel E. González](https://github.com/GabrielEGonzalez)
📚 Estudiante de Ingeniería en Informática
💡 Apasionado por el desarrollo web, IA y sistemas inteligentes.

---