from PIL import Image
import os
carpeta_collage=input("Ingrese una carpeta que contenga al menos 9 imagenes: ")
resolucion_collage=int(input("Ingrese la resolucion que se usara en este collage: "))
lista=[]

if os.path.isdir(carpeta_collage):

    for archivo in os.listdir(carpeta_collage):

        ruta_completa=os.path.join(carpeta_collage,archivo)

        if os.path.isfile(ruta_completa) and archivo.lower().endswith(('.png','.jpg','.jpeg','.gif')):
            lista.append(ruta_completa)
else:
    print("la carpeta no existe o no se puede acceder a ella")
if len(lista) >= 9:
    collage= Image.new('RGB',(resolucion_collage, resolucion_collage))
    tamaño_imagen=resolucion_collage//3
    x=0
    y=0
    for i in range(len(lista)):
        imagen=Image.open(lista[i])
        imagen=imagen.resize((tamaño_imagen,tamaño_imagen))
        collage.paste(imagen,(x,y))
        if i%3==2:
            x=0
            y+=tamaño_imagen
        else:
            x+=tamaño_imagen
    collage.show()
else:
    print("No hay suficientes imagenes")
def ReSize():
    for i in lista:
        img = Image.open(i)
        width, height= img.size
        if width > height:
            height= int((200/width)*height)
            width=200
        else:
            width= int((200/height)*width)
            height=200
        img=img.resize((width,height))
ReSize()