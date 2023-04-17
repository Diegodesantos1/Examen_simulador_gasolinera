import threading
import time
import random


class Coche(threading.Thread):
    def __init__(self, id, gasolinera):
        threading.Thread.__init__(self)
        self.id = id
        self.gasolinera = gasolinera
        self.tiempo = 0
        self.surtidor = None
        self.cola = None
        self.cola_pago = None
        self.cola_salida = None
        self.estado = "Llegando"
        self.start()

    def run(self):
        self.tiempo = time.time()
        self.gasolinera.llega(self)
        self.gasolinera.ocupar_surtidor(self)
        self.gasolinera.pagar(self)
        self.gasolinera.salir(self)
        self.tiempo = time.time() - self.tiempo
        print(f"El coche {self.id} ha tardado {self.tiempo} segundos en repostar")

class Gasolinera:
    def __init__(self, surtidores):
        self.surtidores = surtidores
        self.surtidores_libres = surtidores
        self.surtidores_ocupados = 0
        self.cola = []
        self.cola_pago = []
        self.cola_salida = []
        self.tiempo = 0
        self.tiempo_medio = 0
        self.coche = 0

    def llega(self, coche):
        print(f"El coche {coche.id} ha llegado a la gasolinera")
        time.sleep(random.randint(1, 15)/100.0)

    def ocupar_surtidor(self, coche):
        print("El coche %d se ha puesto en el surtidor" % coche.id)
        coche.surtidor = self.surtidores_libres
        self.surtidores_libres -= 1
        self.surtidores_ocupados += 1
        time.sleep(random.randint(5, 10)/100.0)
        self.surtidores_libres += 1
        self.surtidores_ocupados -= 1
        print(f"El coche {coche.id} ha terminado de repostar")

    def pagar(self, coche):
        print(f"El coche {coche.id} se ha puesto en la cola de pago")
        self.cola_pago.append(coche)
        time.sleep(3)
        print("El coche %d ha terminado de pagar" % coche.id)

    def salir(self, coche):
        print("El coche %d se ha puesto en la cola de salida" % coche.id)
        self.cola_salida.append(coche)
        time.sleep(1)
        print("El coche %d ha salido de la gasolinera" % coche.id)


def iniciar():
    gasolinera = Gasolinera(1)
    for i in range(50):
        Coche(i, gasolinera)