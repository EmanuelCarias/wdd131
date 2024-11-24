from PIL import Image

# Ruta de la imagen original
input_path = r"images\ave_guatemela.jpg"

# Ruta de la imagen convertida a WebP
output_path = r"images\ave_guatemela.webp"

# Convertir a WebP
image = Image.open(input_path)
image.save(output_path, "webp")

print(f"Imagen convertida a WebP y guardada como: {output_path}")
