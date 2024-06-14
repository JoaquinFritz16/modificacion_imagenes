from PIL import Image
import os
imagen=input("Ingrese la ruta de la imagen: ")
if imagen.endswith('.jpg') or imagen.endswith('.png') or imagen.endswith('.jpeg'):
    if imagen.endswith('.png'):
        im=Image.open(imagen)
        nombre_jpg=imagen.replace('.png','.jpg')
        im.convert('RGB').save(nombre_jpg, quality=95)
        imagen=nombre_jpg
    print("La imagen es un archivo local")
    angulo=input("Ingrese el grado (º) de rotacion: ")
    imagen_abierta=Image.open(imagen)
    imagen_rotada=imagen_abierta.rotate(int(angulo))
    nueva_carpeta=r'\\institutodc01\d48125437\modificacion_imagenes\images_rotate'
    if not os.path.exists(nueva_carpeta):
        os.makedirs(nueva_carpeta)
    imagen_rotada.save(nueva_carpeta+r'\imagen_rotada.jpg')
else:
    print("La imagen no es un archivo local")