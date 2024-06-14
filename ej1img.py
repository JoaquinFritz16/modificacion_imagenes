from PIL import Image
from tabulate import tabulate

imagen = input("Ingresar la ruta de la imagen: ")

if imagen.endswith('.jpg') or imagen.endswith('.png') or imagen.endswith('.jpeg'):
    print("La imagen es un archivo local")
    
    imagen_abierta = Image.open(imagen)
    imagen_abierta.show()
    print(f"Abrir la imagen: {imagen_abierta}")
    print(f"Tamaño de la imagen: {imagen_abierta.size}")
    print(f"Nombre de archivo: {imagen_abierta.filename}")
    print(f"Formato de la imagen: {imagen_abierta.format}")
    table=[["Abrir imagen: ", imagen_abierta],
           ["Tamaño img: ", imagen_abierta.size],
           ["Nombre archivo: ",imagen_abierta.filename],
           ["Formato img: ", imagen_abierta.format]]
    print(tabulate(table))
else:
    print("La imagen no se encuentra en esa ruta")
