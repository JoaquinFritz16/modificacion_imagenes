from PIL import Image, ImageFilter

# Carga la imagen
img = Image.open("imagenes/pikachu.png").convert("RGB")
# Aplica el filtro gaussiano
blurred_img = img.filter(ImageFilter.GaussianBlur(radius=2))
# Muestra la imagen borrosa
blurred_img.show()
