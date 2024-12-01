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

const temples = [{
        templeName: "Aba Nigeria",
        location: "Aba, Nigeria",
        dedicated: "2005, August, 7",
        area: 11500,
        imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/aba-nigeria/400x250/aba-nigeria-temple-lds-273999-wallpaper.jpg"
    },
    {
        templeName: "Manti Utah",
        location: "Manti, Utah, United States",
        dedicated: "1888, May, 21",
        area: 74792,
        imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/manti-utah/400x250/manti-temple-768192-wallpaper.jpg"
    },
    {
        templeName: "Payson Utah",
        location: "Payson, Utah, United States",
        dedicated: "2015, June, 7",
        area: 96630,
        imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/payson-utah/400x225/payson-utah-temple-exterior-1416671-wallpaper.jpg"
    },
    {
        templeName: "Yigo Guam",
        location: "Yigo, Guam",
        dedicated: "2020, May, 2",
        area: 6861,
        imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/yigo-guam/400x250/yigo_guam_temple_2.jpg"
    },
    {
        templeName: "Washington D.C.",
        location: "Kensington, Maryland, United States",
        dedicated: "1974, November, 19",
        area: 156558,
        imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/washington-dc/400x250/washington_dc_temple-exterior-2.jpeg"
    },
    {
        templeName: "Lima Perú",
        location: "Lima, Perú",
        dedicated: "1986, January, 10",
        area: 9600,
        imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/lima-peru/400x250/lima-peru-temple-evening-1075606-wallpaper.jpg"
    },
    {
        templeName: "Mexico City Mexico",
        location: "Mexico City, Mexico",
        dedicated: "1983, December, 2",
        area: 116642,
        imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/mexico-city-mexico/400x250/mexico-city-temple-exterior-1518361-wallpaper.jpg"
    },
    // Add more temple objects here...
];

// Elementos clave
const container = document.getElementById("temple-cards-container");
const navButtons = document.querySelectorAll("button[data-filter]");
const filterTitle = document.getElementById("filter-title");
// Generar tarjetas de templos
function displayTemples(filter = "all") {
    container.innerHTML = "";
    // Cambiar título según el filtro seleccionado
    switch (filter) {
        case "old":
            filterTitle.textContent = "Old";
            break;
        case "new":
            filterTitle.textContent = "New";
            break;
        case "large":
            filterTitle.textContent = "Large";
            break;
        case "small":
            filterTitle.textContent = "Small";
            break;
        default:
            filterTitle.textContent = "Home";
            break;
    }
    const filteredTemples = temples.filter((temple) => {
        const dedicatedYear = new Date(temple.dedicated).getFullYear();
        switch (filter) {
            case "old":
                return dedicatedYear < 1900;
            case "new":
                return dedicatedYear > 2000;
            case "large":
                return temple.area > 90000;
            case "small":
                return temple.area < 10000;
            default:
                return true;
        }
    });

    filteredTemples.forEach((temple) => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
              <img src="${temple.imageUrl}" alt="${temple.templeName}" loading="lazy">
              <h2>${temple.templeName}</h2>
              <p>Location: ${temple.location}</p>
              <p>Dedicated: ${temple.dedicated}</p>
              <p>Area: ${temple.area} sq ft</p>
          `;
        container.appendChild(card);
    });
}

// Manejar filtros
navButtons.forEach((button) => {
    button.addEventListener("click", () => {
        displayTemples(button.dataset.filter);
    });
});

// Mostrar todos al cargar
displayTemples();