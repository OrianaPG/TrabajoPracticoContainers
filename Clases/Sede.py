from Container.Container import Container

class Sede:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.containers = []

    def get_ubicacion(self):
        return self.ubicacion
    
    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def get_containers(self):
        return self.__containers

    def set_barcos(self, containers: Container):
        self.__containers.append(containers)

    def agregar_container(self, container: Container):
        self.__containers.append(container)

    def eliminar_container(self, container: Container):
        self.__containers.remove(container)