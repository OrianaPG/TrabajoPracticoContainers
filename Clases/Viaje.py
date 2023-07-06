from .Container.Container import Container

class Viaje:
    def __init__(self, contenedor: Container, distancia, puertaAPuerta):
        self.__contenedor = contenedor
        self.__contenedorLleno = contenedor.estaCompleto()
        self.__distancia = distancia
        self.__puertaAPuerta = puertaAPuerta

    def getContenedor(self):
        return self.__contenedor
    
    def getContenedorLleno(self):
        return self.__contenedorLleno
    
    def getDistancia(self):
        return self.__distancia
    
    def getPuertaAPuerta(self):
        return self.__puertaAPuerta
