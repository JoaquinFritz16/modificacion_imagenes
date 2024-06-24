from PIL import Image
import os

image=input("Ingrese la ruta de la imagen (debe tener la extension png): ")
if image.endswith('.png'):
    img=Image.open(image).convert('RGB')

    width, height= img.size
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r = 255 - r
            g = 255 - g
            b = 255 - b
            prom=sum([r,g,b])//3
            if prom<128:
                r=0
                g=0
                b=0
            else:
                r=255
                g=255
                b=255
            img.putpixel((x,y),(r,g,b))
    nombre_archivo=os.path.basename(image)+'BN.png'
    nombre_carpeta='ImagenesFiltradas'
            
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
    ruta_archivo=os.path.join(nombre_carpeta,nombre_archivo)
    img.save(ruta_archivo)
    print(f"Imagen guardada en {nombre_carpeta}")
else:
    print("La ruta ingresada no es válida")