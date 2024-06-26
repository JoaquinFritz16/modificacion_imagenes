from PIL import Image
from PIL import Image
import os

def gaussian(img, mascara):
    img = img.convert('RGB')
    pixels = img.load()
    width, height = img.size

    kernel_size = len(mascara)
    margen = kernel_size // 2
    

    for y in range(margen, height - margen):
        for x in range(margen, width - margen):
            totalR =0
            totalG =0
            totalB =0
            for i in range(-margen, margen + 1):
                for j in range(-margen, margen + 1):
                    auxX = x + i
                    auxY = y + j
                    r, g, b = pixels[auxX, auxY]
                    weight = mascara[j + margen][i + margen]

                    totalR += r * weight
                    totalG += g * weight
                    totalB += b * weight

            pixels[x, y] = (int(totalR), int(totalG), int(totalB))

    return img

image = input("Ingrese la ruta de la imagen: ")
if image.endswith('.png') or image.endswith('.jpg') or image.endswith('.gif'):
    
    mascara_sigma2 = [
    [0.000036, 0.000363, 0.001446, 0.002290, 0.001446, 0.000363, 0.000036],
    [0.000363, 0.003676, 0.014652, 0.023228, 0.014652, 0.003676, 0.000363],
    [0.001446, 0.014652, 0.058488, 0.092651, 0.058488, 0.014652, 0.001446],
    [0.002290, 0.023228, 0.092651, 0.146768, 0.092651, 0.023228, 0.002290],
    [0.001446, 0.014652, 0.058488, 0.092651, 0.058488, 0.014652, 0.001446],
    [0.000363, 0.003676, 0.014652, 0.023228, 0.014652, 0.003676, 0.000363],
    [0.000036, 0.000363, 0.001446, 0.002290, 0.001446, 0.000363, 0.000036]
    ]

    if not os.path.isfile(image):
        print(f"El archivo {image} no se encuentra.")
    else:
        
        img = Image.open(image)

        img_gaussiano = gaussian(img, mascara_sigma2)

        img.show()
        img_gaussiano.show()
        nombre_archivo=os.path.basename(image)+'Gaussian.png'
        nombre_carpeta='ImagenesFiltradas'
            
        if not os.path.exists(nombre_carpeta):
            os.makedirs(nombre_carpeta)
        ruta_archivo=os.path.join(nombre_carpeta,nombre_archivo)
        img_gaussiano.save(ruta_archivo)
else:
    print("El archivo no es una imagen PNG o JPG.")