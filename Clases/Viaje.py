from .Container.Container import Container

class Viaje:
    def __init__(self, contenedor, distancia, puertaAPuerta):
        self.__contenedor = contenedor
        self.__contenedorLleno = contenedor.estaCompleto()
        self.distancia = distancia
        self.puertaAPuerta = puertaAPuerta

    def getContenedor(self):
        return self.__contenedor
    
    def getContenedorLleno(self):
        return self.__contenedorLleno
