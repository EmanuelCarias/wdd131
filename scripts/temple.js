// Mostrar la última fecha de modificación
// Display the current year
document.getElementById('currentyear').textContent = new Date().getFullYear();

// Display the last modified date of the document
document.getElementById('lastModified').textContent = 'Last modified: ' + document.lastModified;
// Funcionalidad de menú hamburguesa
const nav = document.querySelector("nav ul");
const toggleMenu = document.createElement("button");
toggleMenu.textContent = "☰";
toggleMenu.classList.add("hamburger");
document.querySelector("header").prepend(toggleMenu);

toggleMenu.addEventListener("click", () => {
    nav.classList.toggle("visible");
});