from PIL import Image

# Ruta de la imagen original
input_image_path = "images/ave_guatemela.jpg"  # Cambia esto por tu imagen original

# Ruta para guardar las versiones redimensionadas
large_image_path = "images/hero-large.webp"
small_image_path = "images/hero-small.webp"

# Abrir la imagen original
image = Image.open(input_image_path)

# Redimensionar a una versión grande (por ejemplo, 1200x800 píxeles)
large_image = image.resize((1200, 800))  # Ajusta las dimensiones según necesites
large_image.save(large_image_path, format="WEBP")

# Redimensionar a una versión pequeña (por ejemplo, 600x400 píxeles)
small_image = image.resize((600, 400))  # Ajusta las dimensiones según necesites
small_image.save(small_image_path, format="WEBP")

print("Imágenes generadas: ")
print(f"Versión grande guardada en: {large_image_path}")
print(f"Versión pequeña guardada en: {small_image_path}")
