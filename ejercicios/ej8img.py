from PIL import Image
import os
def gaussiano(img):
    img = img.copy()  
    pixels = img.load()  

    width, height = img.size

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            totalPixels = 0
            totalR = 0
            totalG = 0
            totalB = 0

            for j in range(-1, 2):
                for i in range(-1, 2):
                    auxX = x + i
                    auxY = y + j

                    r, g, b = pixels[auxX, auxY]
                    totalR += r
                    totalG += g
                    totalB += b
                    totalPixels += 1

            totalR //= totalPixels
            totalG //= totalPixels
            totalB //= totalPixels

            pixels[x, y] = (totalR, totalG, totalB)

    return img

image=input("Ingrese la ruta de la imagen (debe tener la extension '.png'): ")
pixel_size=int(input("Ingrese el tamaño de pixelado: "))
if image.endswith('.png'):
    img = Image.open(image).convert('RGB')

    nombre_archivo=os.path.basename(image)+'Pixelator.png'
    nombre_carpeta='ImagenesFiltradas'
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
    ruta_archivo=os.path.join(nombre_carpeta,nombre_archivo)
    print(f"Imagen guardada en {nombre_carpeta}")
else:
    print("La ruta de la imagen no es valida (Recuerda que debe tener la extension '.png')")