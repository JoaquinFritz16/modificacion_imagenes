from PIL import Image
import os

imagen = input("Ingrese la ruta de la imagen (debe tener la extensión .png, .jpg o .jpeg): ")
if imagen.endswith(('.jpg', '.png', '.jpeg')):
    if imagen.endswith('.png'):
        im = Image.open(imagen)
        nombre_jpg = imagen.replace('.png', '.jpg')
        im.convert('RGB').save(nombre_jpg, quality=95)
        imagen = nombre_jpg
    
    print("La imagen es un archivo local")
    angulo = input("Ingrese el grado (º) de rotación: ")
    angulo = int(angulo)
    imagen_abierta = Image.open(imagen)
    imagen_rotada = imagen_abierta.rotate(angulo)
    
    nombre_archivo, extension = os.path.splitext(os.path.basename(imagen))
    nuevo_nombre = f"{nombre_archivo}Rot{extension}"
    
    nueva_carpeta = 'images_rotate'
    if not os.path.exists(nueva_carpeta):
        os.makedirs(nueva_carpeta)
    
    ruta_archivo = os.path.join(nueva_carpeta, nuevo_nombre)
    imagen_rotada.save(ruta_archivo)
    imagen_rotada.show()
    
    print(f"Imagen rotada guardada en {ruta_archivo}")
else:
    print("La imagen no es un archivo local o no tiene una extensión válida.")