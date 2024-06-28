from PIL import Image
import os

while True:
    i = 0
    imagen = input("Ingrese la ruta de la imagen a utilizar (o escriba 'salir' para terminar): ")
    
    if imagen.lower() == 'salir':
        print("Saliendo del programa...")
        break
    if imagen.endswith('.jpg') or imagen.endswith('.png') or imagen.endswith('.jpeg'):
        if os.path.isfile(imagen):
            print("La imagen es un archivo local")
            imagen_abierta = Image.open(imagen)
            ancho_imagen, alto_imagen=imagen_abierta.size 
            print(f"Recuerda que el ancho de la imagen es: {ancho_imagen}")
            print(f"Recuerda que el alto de la imagen es: {alto_imagen}")
            while True:
                coordenada_inicial_x = int(input("Ingrese la coordenada inicial en x: "))
                coordenada_inicial_y = int(input("Ingrese la coordenada inicial en y: "))
                coordenada_ancho = int(input("Ingrese la coordenada de ancho (x final): "))
                coordenada_altura = int(input("Ingrese la coordenada de altura (y final): "))
                if (coordenada_inicial_x < 0 or coordenada_inicial_y < 0 or
                    coordenada_ancho > ancho_imagen or coordenada_altura > alto_imagen or
                    coordenada_inicial_x >= coordenada_ancho or coordenada_inicial_y >= coordenada_altura):
                            print("Las coordenadas exceden los límites de la imagen. Saliendo del programa...")
                            break
                croppedIm = imagen_abierta.crop((coordenada_inicial_x, coordenada_inicial_y, coordenada_ancho, coordenada_altura))
                
                nueva_carpeta = 'recortes'
                
                if not os.path.exists(nueva_carpeta):
                    os.makedirs(nueva_carpeta)
                
                nueva_ruta = os.path.join(nueva_carpeta, f'recorte{i+1}.png')
                
                croppedIm.save(nueva_ruta)
                print(f"Recorte guardado como recorte{i+1}.png en {nueva_carpeta}")
                croppedIm.show()
                    
                respuesta = input("¿Desea realizar otro recorte? (s/n): ").lower()
                if respuesta != 's':
                    break
        else:
             print("Ese archivo no existe")
    else:
        print("Eso no es una imagen (deberia termninar en .jpg, .png, .jpeg)")
    