// Mostrar la última fecha de modificación
// Display the current year
document.getElementById('currentyear').textContent = new Date().getFullYear();

// Display the last modified date of the document
document.getElementById('lastModified').textContent = 'Last modified: ' + document.lastModified;

document.addEventListener("DOMContentLoaded", () => {
    // Variables estáticas
    const temperature = 10; // en °C
    const windSpeed = 5; // en km/h

    // Actualizar pie de página
    const lastModified = document.lastModified;
    document.getElementById("last-modified").textContent = lastModified;

    // Calcular el factor de enfriamiento del viento
    const calculateWindChill = (temp, speed) => {
        if (temp <= 10 && speed > 4.8) {
            return (
                13.12 +
                0.6215 * temp -
                11.37 * Math.pow(speed, 0.16) +
                0.3965 * temp * Math.pow(speed, 0.16)
            ).toFixed(2);
        }
        return "N/A";
    };

    // Mostrar el cálculo
    const windChill = calculateWindChill(temperature, windSpeed);
    document.getElementById("wind-chill").textContent = windChill;
});