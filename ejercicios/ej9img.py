from PIL import Image
import os
def pixelate_image(img, pixel_size):
    width, height = img.size
    img_pixelated = img.copy()
    for y in range(0, height, pixel_size):
        for x in range(0, width, pixel_size):
            r_total=0
            g_total=0
            b_total=0
            count=0
            for y2 in range(pixel_size):
                for x2 in range(pixel_size):
                    if x+x2 < width and y+y2 < height:
                        r, g, b = img.getpixel((x+x2,y+y2))
                        r_total += r
                        g_total += g
                        b_total += b
                        count += 1
            if count!=0:
                r_avg = r_total // count
                g_avg = g_total // count
                b_avg = b_total // count
            
                for y2 in range(pixel_size):
                    for x2 in range(pixel_size):
                        if x+x2 < width and y+y2 < height:
                            img_pixelated.putpixel((x+x2,y+y2), (r_avg, g_avg, b_avg))
    return img_pixelated

image=input("Ingrese la ruta de la imagen (debe tener la extension '.png' o '.gif'): ")
pixel_size=int(input("Ingrese el tamaño de pixelado: "))
if image.endswith('.png') or image.endswith('.gif'):
    img = Image.open(image).convert('RGB')
    img_pixelated = pixelate_image(img, pixel_size)

    nombre_archivo=os.path.basename(image)+'Pixelator.png'
    nombre_carpeta='ImagenesFiltradas'
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
    ruta_archivo=os.path.join(nombre_carpeta,nombre_archivo)
    img_pixelated.show()
    img_pixelated.save(ruta_archivo)
    print(f"Imagen guardada en {nombre_carpeta}")
else:
    print("La ruta de la imagen no es valida (Recuerda que debe tener la extension '.png')")