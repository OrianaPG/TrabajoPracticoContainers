from Sede import Sede
from Barcos.Barco import Barco
from Camion import Camion
from Container.Container import Container

class Empresa:
    def __init__(self):
        self.__sedes = []
        self.__camiones_disponibles = 5
        self.barcos = []
        self.camiones = []
        self.contenedores = []
        self.viajesContenedor = []#va a guardar todos los viajes de los contenedores

    def get_sedes(self):
        return self.__sedes

    def set_sedes(self, sede: Sede):
        self.__sedes.append(sede)

    def get_barcos(self):
        return self.barcos

    def set_barcos(self, barcos: Barco):
        self.barcos.append(barcos)

    def get_camiones(self):
        return self.camiones

    def set_camiones(self, camiones: Camion):
        self.camiones.append(camiones)

    def get_camiones_disponibles(self):
        disponible = 0
        for i in self.get_camiones:
            if Camion.get_cargado == False:
                disponible = disponible + 1
        return disponible
    
    def get_containers(self):
        return self.contenedores

    def set_containers(self, containers: Container):
        self.contenedores.append(contenedores)

    def enviar_container(self, container: Container):
        self.viajesContenedor.append(container)

    def agregarBarco(self, barco):
        self.barcos.append(barco)

    def agregarCamion(self, camion):
        self.camiones.append(camion)

    def agregarContenedor(self, contenedor):
        self.contenedores.append(contenedor)

    def calcularPrecioEnvio(self, distancia, container_completo, peso):
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

      return precio

    def encontrarContenedorMasViajesCompleto(self):
        #encuentra el contenedor que hizo mas viajes completo
        contadorContainer = {}
        for contenedor in self.viajesContenedor:
           if contenedor.estaCompleto():
              contenedorID = contenedor.getID()
              contadorContainer[contenedorID] = contadorContainer.get(contenedorID, 0) + 1 #busca si ya esta el id en la lista, si no devuelve 0

        contenedorMasViajesCompleto = max(contadorContainer, key=contadorContainer.get) #max busca el mayor valor segun contdorContiner.get
        return contenedorMasViajesCompleto                                              #el .get obtiene los valores asociados a las claves en la lista

    def encontrarBarcoMayorDistancia(self):
        #encontrar el barco que hizo la mayor distancia
        mayorDistancia = -1
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
