from PIL import Image

# Ruta de la imagen original y la imagen de salida
image_path = r"C:\Users\user\Desktop\byu\wdd131\project\images\cake_logo.ico"  # Asegúrate de usar el nombre correcto
output_path = r"C:\Users\user\Desktop\byu\wdd131\project\images\cake_logo_colored.ico"

# Abre la imagen y conviértela a formato editable
image = Image.open(image_path).convert("RGBA")

# Define tus colores (en formato RGB)
primary_color = (210, 105, 30)  # #d2691e
secondary_color = (245, 166, 35)  # #f5a623


# Redimensiona la imagen a 256x256 píxeles
image = image.resize((256, 256), Image.LANCZOS)

# Obtén los datos de los píxeles
pixels = image.load()
width, height = image.size

# Cambia los colores según el esquema
for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]  # Obtén el color y la opacidad del píxel
        if a > 0:  # Solo modifica píxeles visibles
            if r > 200 and g > 200 and b > 200:  # Reemplaza blancos
                pixels[x, y] = primary_color + (a,)
            else:
                pixels[x, y] = secondary_color + (a,)

# Guarda la nueva imagen como archivo .ico
image.save(output_path, format="ICO")
print(f"Imagen guardada como: {output_path}")