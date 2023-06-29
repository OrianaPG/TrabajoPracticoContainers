from .Container.Container import Container

class Viaje:
    def __init__(self, contenedor):
        self.__contenedor = contenedor
        self.__contenedorLleno = contenedor.estaCompleto()
    def getContenedor(self):
        return self.__contenedor
    def getContenedorLleno(self):
        return self.__contenedorLleno
