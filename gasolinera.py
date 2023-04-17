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
        print("El coche %d ha tardado %f segundos" % (self.id, self.tiempo))


