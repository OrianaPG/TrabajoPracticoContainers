from abc import ABC

from ..Barcos.Barco import Barco
from ..Container.Container import Container
from ..MockObj.GPSMock import GPSMock

class Basico(Barco, ABC):
    def __init__(self, id, max_container, max_peso):
        super().__init__(id, max_container, max_peso)

    def descargar(self):
        cont = Container()
        li = list()
        while self.get_containers():
            cont = self.get_containers().pop(0)
            li.append(cont)

            # bajar el peso del contenedor

        return li

    def kilometros_recorridos(self, inicio, destino):
        distancia = GPSMock(inicio, destino)
        self.set_distancia(self.get_distancia() + distancia)
        return distancia
