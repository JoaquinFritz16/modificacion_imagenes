import os
from PIL import Image

Square_Fit_Size= 300
logo_filename='imagenes/boca_marca_agua.png'

logo_im = Image.open(logo_filename).convert('RGBA')
logoWidth, logoHeight = logo_im.size

imagen = input("Ingresar la ruta de la imagen (debe ser '.png'): ")
if imagen.endswith('.png'):
    print("La imagen es un archivo local")
    
    imagen_abierta = Image.open(imagen).convert('RGBA')
    width, height = imagen_abierta.size

    margen=50
    opciones_position={
        'top-left':(margen, margen),
        'top-right':(width - logoWidth - margen, margen),
        'bottom-left':(margen, height - logoHeight - margen),
        'bottom-right':(width - logoWidth - margen , height - logoHeight - margen),
    }
    for key, value in opciones_position.items():
        print(f"{key}. {value}")
    eleccion=int(input("Opcion: "))
    position=opciones_position[list(opciones_position.keys())[eleccion-1]]
    imagen_marca=imagen_abierta.copy()
    imagen_marca.paste(logo_im, position, logo_im)
    imagen_marca.show()

    
    nueva_carpeta='marca_de_agua'
    if not os.path.exists(nueva_carpeta):
        os.makedirs(nueva_carpeta)
    nombre_archivo=os.path.basename(imagen)
    nombre_salida=os.path.join(nueva_carpeta,f"{position}_{nombre_archivo}")
    imagen_marca.save(nombre_salida)
    print(f"Imagen guardada en {nueva_carpeta}")
else:
    print("Eso no es una imagen (deberia termninar en .png)")