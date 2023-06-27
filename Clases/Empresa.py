from Sede import Sede
from Barcos.Barco import Barco
from Camion import Camion
from Container.Container import Container

class Empresa:
    def __init__(self):
        self.__sedes = []
        self.__barcos = []
        self.__camiones = []
        self.__camiones_disponibles = 5
        self.__containers = []

    def get_sedes(self):
        return self.__sedes

    def set_sedes(self, sede: Sede):
        self.__sedes.append(sede)

    def get_barcos(self):
        return self.__barcos

    def set_barcos(self, barcos: Barco):
        self.__barcos.append(barcos)

    def get_camiones(self):
        return self.__camiones

    def set_camiones(self, camiones: Camion):
        self.__camiones.append(camiones)

    def get_camiones_disponibles(self):
        disponible = 0
        for i in self.get_camiones:
            if Camion.get_cargado == False:
                disponible = disponible + 1
        return disponible
    
    def get_containers(self):
        return self.__containers

    def set_containers(self, containers: Container):
        self.__containers.append(containers)

    def enviar_container(self, origen: Sede, destino: Sede, container: Container):
        pass
