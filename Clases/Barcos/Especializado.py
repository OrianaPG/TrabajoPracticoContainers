from abc import ABC

from Barcos.Barco import Barco
from MockObj.GPSMock import GPSMock

class Especializado(Barco, ABC):
    def __init__(self):
        super().__init__()
        self.set_especial(True)

    def kilometros_recorridos(self, inicio, destino):
        distancia = GPSMock(inicio, destino)
        self.set_distancia(self.get_distancia() + distancia)
        return distancia
