from PIL import Image


imagen = input("Ingresar imagen: ")

if imagen.endswith('.jpg'):
    print("La imagen es un archivo local")
    imagen_ruta = f'imagenes/{imagen}'
    
    zenon_image = Image.open(imagen_ruta)
    print(f"Abrir la imagen: {zenon_image}")
    print(f"Tamaño de la imagen: {zenon_image.size}")
    print(f"Nombre de archivo: {zenon_image.filename}")
    print(f"Formato de la imagen: {zenon_image.format}")
else:
    print("La imagen es una URL")
