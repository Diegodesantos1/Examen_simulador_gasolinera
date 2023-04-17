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

class Gasolinera:
    def __init__(self, surtidores):
        self.surtidores = surtidores
        self.surtidores_libres = surtidores
        self.surtidores_ocupados = 0
        self.cola = []
        self.cola_pago = []
        self.cola_salida = []
        self.coche = 0

    def llega(self, coche):
        print(f"El coche {coche.id} ha llegado a la gasolinera")

    def ocupar_surtidor(self, coche):
        print(f"El coche {coche.id} se ha puesto en la cola de surtidores")
        coche.surtidor = self.surtidores_libres
        self.surtidores_libres -= 1
        self.surtidores_ocupados += 1
        self.surtidores_libres += 1
        self.surtidores_ocupados -= 1
        time.sleep(random.randint(5,10))
        print(f"El coche {coche.id} ha terminado de repostar")

    def pagar(self, coche):
        print(f"El coche {coche.id} se ha puesto en la cola de pago")
        self.cola_pago.append(coche)
        time.sleep(3)
        print(f"El coche {coche.id} ha pagado")

    def salir(self, coche):
        print(f"El coche {coche.id} se ha puesto en la cola de salida")
        self.cola_salida.append(coche)
        time.sleep(1)


def iniciar():
    gasolinera = Gasolinera(1)
    tiempo_inicial = time.time()
    for i in range(50):
        Coche(i, gasolinera)
    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    time.sleep(30)
    tiempo_final = (tiempo_ejecucion*20000)
    print(f"El tiempo que han tardado todos los coches en repostar ha sido de {tiempo_final} minutos")