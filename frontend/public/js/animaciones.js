// Importar funciones de Motion One
const { animate, scroll, inView, stagger } = motion;

// 🟢 Animar el encabezado al cargar
window.addEventListener("load", () => {
  // Logo aparece desde arriba
  animate("header img", { opacity: [0, 1], y: [-50, 0] }, { duration: 1 });

  // Texto principal (Urban Market)
  animate("header h1, header p", 
    { opacity: [0, 1], y: [30, 0] }, 
    { delay: stagger(0.2), duration: 0.8, easing: "ease-out" }
  );

  // Botones de registro
  animate(".regis a", 
    { opacity: [0, 1], scale: [0.8, 1] }, 
    { delay: stagger(0.15), duration: 0.5 }
  );
});

// 🟡 Efecto de entrada al hacer scroll (para las secciones)
inView(".hero, .banner-img, #comentario, footer", ({ target }) => {
  animate(target, { opacity: [0, 1], y: [40, 0] }, { duration: 0.7, easing: "ease-out" });
});

// 🔵 Animación de los productos (cuando ya están en el DOM)
const observer = new MutationObserver(() => {
  const cards = document.querySelectorAll(".head-card");
  if (cards.length > 0) {
    animate(".head-card", 
      { opacity: [0, 1], y: [20, 0] }, 
      { delay: stagger(0.1), duration: 0.5, easing: "ease-out" }
    );
    observer.disconnect();
  }
});
observer.observe(document.getElementById("contenedor"), { childList: true });

// 🟣 Hover de los botones
document.addEventListener("mouseover", e => {
  if (e.target.tagName === "BUTTON") {
    animate(e.target, { scale: 1.1 }, { duration: 0.2 });
  }
});
document.addEventListener("mouseout", e => {
  if (e.target.tagName === "BUTTON") {
    animate(e.target, { scale: 1 }, { duration: 0.2 });
  }
});

// 💫 Movimiento leve del banner (decorativo)
animate(".banner-img img", 
  { y: [0, -10, 0] }, 
  { duration: 6, repeat: Infinity, easing: "ease-in-out", delay: stagger(0.3) }
);
