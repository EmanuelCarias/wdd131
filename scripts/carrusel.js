// Mostrar la última fecha de modificación
// Display the current year
//document.getElementById('currentyear').textContent = new Date().getFullYear();

// Display the last modified date of the document
//document.getElementById('lastModified').textContent = 'Last modified: ' + document.lastModified;
// Funcionalidad de menú hamburguesa
const nav = document.querySelector("nav ul");
const toggleMenu = document.createElement("button");
const menuPopup = document.getElementById("menu-popup");
toggleMenu.textContent = "☰";
toggleMenu.classList.add("hamburger");
document.querySelector("header").prepend(toggleMenu);

toggleMenu.addEventListener("click", () => {
    menuPopup.style.display = menuPopup.style.display === "flex" ? "none" : "flex";
});
// Cerrar el menú si se hace clic fuera del contenido
menuPopup.addEventListener("click", (e) => {
    if (e.target === menuPopup) { // Solo cierra si haces clic fuera del contenido
        menuPopup.style.display = "none";
    }
});
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('.carousel img');
    let currentIndex = 0;

    function showNextImage() {
        images[currentIndex].classList.remove('active'); // Oculta la imagen actual
        currentIndex = (currentIndex + 1) % images.length; // Avanza al siguiente índice
        images[currentIndex].classList.add('active'); // Muestra la siguiente imagen
    }

    // Inicializa la primera imagen
    images[currentIndex].classList.add('active');

    // Configura el intervalo para el cambio automático
    setInterval(showNextImage, 3000); // Cambia cada 3 segundos
});