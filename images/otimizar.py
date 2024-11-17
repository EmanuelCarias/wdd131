from PIL import Image
import os

# Carpeta de las imágenes
input_folder = "images/"
output_folder = "optimized_images/"

# Crear la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Optimizar imágenes
for filename in os.listdir(input_folder):
    if filename.endswith(".webp"):
        filepath = os.path.join(input_folder, filename)
        img = Image.open(filepath)
        
        # Reducir calidad y guardar la nueva imagen
        optimized_path = os.path.join(output_folder, filename)
        img.save(optimized_path, "WEBP", quality=60, optimize=True)

        print(f"{filename} optimizada y guardada en {optimized_path}")
