from abc import ABC, abstractmethod
from ..Excepciones.ContainerNoPuedeSubirBarco import ContainerNoPuedeSubirBarco

class Barco(ABC):
    def __init__(self, id, max_container, max_peso):
        self.__id = id
        self.__max_container = max_container
        self.__max_peso = max_peso
        self.__peso = 0
        self.__especial = False
        self.__containers = list()
        self.__distancia_recorrida = 0.0
        self.__sede_inicio = ''
        self.__sede_destino = ''

    def get_id(self):
        return self.__id

    def set_id(self,id):
        self.__id = id

    def get_max_container(self):
        return self.__max_container

    def set_max_container(self, cont):
        self.__max_container = cont

    def get_max_peso(self):
        return self.__max_peso

    def set_max_peso(self, peso):
        self.__max_peso = peso

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    peso = property(get_peso, set_peso)

    def get_especial(self):
        return self.__especial

    def set_especial(self, especial):
        self.__especial = especial

    def get_containers(self):
        return self.__containers

    def cargar(self, container):
        self.__containers.append(container)

    # containers = property(get_containers, cargar)

    def get_distancia(self):
        return self.__distancia_recorrida

    def set_distancia(self, dist):
        self.__distancia_recorrida = dist

    # distancia_recorrida = property(get_distancia, set_distancia)

    def get_sede_inicio(self):
        return self.__sede_destino

    def set_sede_inicio(self, sede):
        self.__sede_inicio = sede

    def get_sede_fin(self):
        return self.__sede_destino

    def set_sede_fin(self, sede):
        self.__sede_destino = sede

    @abstractmethod
    def kilometros_recorridos(self, inicio, destino):
        pass

    @abstractmethod
    def descargar(self):
        pass

    def cargar_container(self, container):
        if self.puedeSubir():
            self.containers.append(container)
        else:
            raise ContainerNoPuedeSubirBarco('El contenedor excede el peso máximo del barco o el barco está ocupado.')
    
    def cantidad_containers(self):
        cantidad = 0
        for c in self.containers:
            cantidad = cantidad + 1
        return cantidad

    def peso_containers(self):
        peso_containers = 0
        for c in self.containers:
            peso_containers = peso_containers + c.peso
        return peso_containers

    def puedeSubir(self, container):
        if len(self.containers) < self.max_container and self.max_peso >= sum(
                [cont.peso for cont in self.containers]) + container.peso:
            return True
        else:
            return False
