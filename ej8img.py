from PIL import Image, ImageFilter
import os

image=input("Ingrese la ruta de la imagen (debe tener la extension '.png'): ")
if image.endswith('.png'):
    img = Image.open(image)
    blurred_img = img.filter(ImageFilter.GaussianBlur(radius=2))
    blurred_img.show()
    nombre_archivo=os.path.basename(image)+'Gaussian.png'
    nombre_carpeta='ImagenesFiltradas'
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
    ruta_archivo=os.path.join(nombre_carpeta,nombre_archivo)
    blurred_img.save(ruta_archivo)
    print(f"Imagen guardada en {nombre_carpeta}")
else:
    print("La ruta de la imagen no es valida (Recuerda que debe tener la extension '.png')")