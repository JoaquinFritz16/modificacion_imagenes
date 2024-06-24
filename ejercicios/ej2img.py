from PIL import Image
import os
imagen = input("Ingresar la imagen: ")

if imagen.endswith('.jpg') or imagen.endswith('.png') or imagen.endswith('.jpeg'):
    print("La imagen es un archivo local")
    
    imagen_abierta = Image.open(imagen)
    nuevo_nombre = 'copia_'+ os.path.basename(imagen)
    nueva_carpeta='images_copy'
    ruta_nueva=os.path.join(nueva_carpeta, nuevo_nombre)
    if not os.path.exists(nueva_carpeta):
        os.makedirs(nueva_carpeta)
    imagen_abierta.save(ruta_nueva)
    print(f"Imagen guardada en {ruta_nueva}")
else:
    print("La imagen no se encuentra en esa ruta")
