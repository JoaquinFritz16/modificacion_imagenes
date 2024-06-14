from PIL import Image
import os
i=0
imagen=input("Ingrese la ruta de la imagen a utilizar: ")
if imagen.endswith('.jpg') or imagen.endswith('.png') or imagen.endswith('.jpeg'):
    print("La imagen es un archivo local")
    imagen_abierta=Image.open(imagen)
    while True:
        coordenada_inicial_x=int(input("Ingrese una coordenada inicial en x: "))
        coordenada_inicial_y=int(input("Ingrese una coordenada inicial en y: "))
        coordenada_ancho=int(input("Ingrese una coordenada de ancho (x final): "))
        coordenada_altura=int(input("Ingrese una coordenada de altura (y final): "))
        croppedIm=imagen_abierta.crop((coordenada_inicial_x,coordenada_inicial_y,coordenada_ancho,coordenada_altura))
        nueva_carpeta=r'\\institutodc01\d48125437\modificacion_imagenes\recortes'
        nueva_ruta=os.path.join(nueva_carpeta,f'recorte{i+1}.png')
        i=i+1
        if not os.path.exists(nueva_carpeta):
            os.makedirs(nueva_carpeta)
        croppedIm.save(nueva_ruta)
        croppedIm.show()
        respuesta=input("Desea continuar con otro recorte? (s/n): ").lower()
        if respuesta == 'n':
            break
else:
    print("No se encontro esa imagen en esa ruta")