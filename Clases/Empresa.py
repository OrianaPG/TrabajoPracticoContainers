from .Sede import Sede
from .Barcos.Barco import Barco
from .Camion import Camion
from .Container.Container import Container
from .Viaje import Viaje
from .MockObj.GPSMock import GPSMock


class Empresa:

    def __init__(self):
        self.barcos = []
        self.camiones = []
        self.contenedores = []
        self.viajesContenedor = [] #va a guardar todos los viajes de los contenedores

    def agregarBarco(self, barco):
        self.barcos.append(barco)

    def agregarCamion(self, camion):
        self.camiones.append(camion)

    def agregarContenedor(self, contenedor):
        self.contenedores.append(contenedor)

    #def enviar_container(self, origen: Sede, destino: Sede, container: Container):
    #   self.viajesContenedor.append(Viaje(container))

    def enviar_barco(self, origen, destino, barco: Barco, puertaAPuerta):
        gps = GPSMock()
        tiempo = gps.calcularTiempoEnHoras(origen, destino)
        distancia = gps.calcularDistancia(origen, destino)

        for container in Barco.get_containers():
            self.viajesContenedor.append(Viaje(container, distancia, puertaAPuerta))
            barco.consumir_combustible(tiempo)
            container.descargar()
            barco.descargar()

    def calcularPrecioEnvio(self, viaje: Viaje):
        
        distancia = viaje.getDistancia()
        puertaAPuerta = viaje.getPuertaAPuerta()
        container_completo = viaje.getContenedorLleno()
        peso = float(viaje.getContenedor().get_peso_actual())
        
        if distancia < 100:
            if container_completo:
                precio = 200000
            else:
                precio = (peso // 100) * 1000
        elif distancia < 1000:
            if container_completo:
                precio = 210000
            else:
                precio = (peso // 100) * 1100
        elif distancia < 10000:
            if container_completo:
                precio = 230000
            else:
                precio = (peso // 100) * 1150
        else:
            if container_completo:
                precio = 250000
            else:
                precio = (peso // 100) * 1500

        if puertaAPuerta:
            return precio + 20000
        else: 
            return precio


    def encontrarContenedorMasViajesCompleto(self):
        #encuentra el contenedor que hizo mas viajes completo
        contadorContainer = {}
        for viaje in self.viajesContenedor:
            if viaje.getContenedorLleno():
                contenedorID = viaje.getContenedor().getID()
                contadorContainer[contenedorID] = contadorContainer.get(contenedorID, 0) + 1 #busca si ya esta el id en la lista, si no devuelve 0

        contenedorMasViajesCompleto = max(contadorContainer, key=lambda contenedorID: contadorContainer[contenedorID])#max compara los valores de la key(los id) y devuelve el id q tiene el mayor valor
        return contenedorMasViajesCompleto # Id del contenedor

    def encontrarBarcoMayorDistancia(self):
        #encontrar el barco que hizo la mayor distancia
        mayorDistancia = float('-inf')
        barcoMayorDistancia = None
        for barco in self.barcos:
            distancia = barco.get_distancia()
            if distancia > mayorDistancia:
                mayorDistancia =distancia
                barcoMayorDistancia = barco
        return barcoMayorDistancia

    def encontrarBarcoMenorDistancia(self):
        #encontrar el barco que hizo la menor distancia
        menorDistancia = float('inf') 
        barcoMenorDistancia = None
        for barco in self.barcos:
            distancia1 = barco.get_distancia()
            if distancia1 < menorDistancia:
                menorDistancia = distancia1
                barcoMenorDistancia = barco
        return barcoMenorDistancia
