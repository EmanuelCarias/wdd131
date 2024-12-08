// Mostrar la última fecha de modificación
// Display the current year
document.getElementById('currentyear').textContent = new Date().getFullYear();

// Display the last modified date of the document
document.getElementById('lastModified').textContent = 'Last modified: ' + document.lastModified;
// Increment the review count
document.addEventListener("DOMContentLoaded", () => {
    const reviewCountKey = "reviewCount";
    const currentCount = localStorage.getItem(reviewCountKey) || 0;
    const newCount = parseInt(currentCount) + 1;
    localStorage.setItem(reviewCountKey, newCount);

    // Display the review count
    const countDisplay = document.getElementById("review-count");
    if (countDisplay) {
        countDisplay.textContent = `You have completed ${newCount} review(s).`;
    }
});