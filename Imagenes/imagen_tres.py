from multiprocessing import Pool #Implementación Pool
from imgurpython import ImgurClient

import os
import timeit
import urllib.request

id_cliente = "bfa0e227a1c5643"
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
cliente = ImgurClient(id_cliente, secreto_cliente)

def descarga_url_img(link):
   print(link)
   # Con esto ya podemos obtener el corte de la url imagen
   nombre_img = link.split('/')[3]
   formato_img = nombre_img.split('.')[1]
   nombre_img = nombre_img.split('.')[0]
   print(nombre_img, formato_img)
   #Guardar en local las imagenes
   url_local = "/Users/Lenovo/Desktop/Images1/{}.{}"
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))

def main():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
   num_images = len(imagenes)
   imagenes_list = [imagen.link for imagen in imagenes]

   with Pool(processes = num_images) as pool: #imp Pool
      print(pool.map(descarga_url_img, imagenes_list))
        
if __name__ == "__main__":
   print("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1)))