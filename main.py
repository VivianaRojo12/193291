import threading

def organizarse(lista):
   size = len(lista)

   if size == 0:
      return

   if size == 1 or size == 2 or size == 3:
      comer(lista[0])
   elif size == 4 or size == 5:
      thread1 = threading.Thread(target=comer,args=[lista[0]])
      thread2 = threading.Thread(target=comer,args=[lista[2]])
      thread1.start()
      thread2.start()
      thread2.join()
   else:
      thread1 = threading.Thread(target=comer,args=[lista[0]])
      thread2 = threading.Thread(target=comer,args=[lista[2]])
      thread3 = threading.Thread(target=comer,args=[lista[4]])
      thread1.start()
      thread1.join()
      thread2.start()
      thread2.join()
      thread3.start()
      thread3.join()

   organizarse(lista)

def comer(item):
   print(item + " tomó los tenedores.")
   print(item + " está comiendo.")
   print(item + " ha terminado de comer.\n")
   lista.pop(lista.index(item))

def sentarse(lista):
   for i in range(len(lista)):
      print(lista[i] + " se ha sentado.")

if __name__ == '__main__':
   lista = []
   lista.append("Viviana")
   lista.append("Ramsés")
   lista.append("Fede")
   lista.append("Luis")
   lista.append("Javi")
   lista.append("Dani")
   lista.append("Yoli de Limon")
   lista.append("Pelusa Caligari")
   lista.append("Saul Hernandez")
 
   print("Los filósofos se han reunido.\n")
   sentarse(lista)
   organizarse(lista)
   print("La cena de los filósofos ha terminado.")