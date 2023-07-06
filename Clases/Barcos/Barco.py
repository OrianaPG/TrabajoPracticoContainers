#from abc import ABC, abstractmethod
from ..Excepciones.ContainerNoPuedeSubirBarco import ContainerNoPuedeSubirBarco
from ..MockObj.GPSMock import GPSMock

class Barco():
    def __init__(self, id, max_container, max_peso, max_combustible, tiene_velas, precioCombustible):
        self.__id = id
        self.__max_container = max_container
        self.__max_peso = max_peso
        self.__peso = 0
        self.__especial = False
        self.__containers = list()
        self.__distancia_recorrida = 0.0
        self.__sede_inicio = ''
        self.__sede_destino = ''

        #para la 2d parte del TP
        self.tiene_velas = tiene_velas
        self.max_combustible = max_combustible
        self.combustible = 0
        self.usandoVela = False
        self.usandoMotor = True
        self.precioCombustible = precioCombustible


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

    # @abstractmethod
    def kilometros_recorridos(self, inicio, destino):
        distancia = GPSMock(inicio, destino)
        self.set_distancia(self.get_distancia() + distancia)
        return distancia

    # @abstractmethod
    def descargar(self):
        self.get_containers().clear() #saca los containers de la lista #? no baja el peso

    def cargar_container(self, container):
        if self.puedeSubir(container):
            self.containers.append(container)
        else:
            raise ContainerNoPuedeSubirBarco('El contenedor excede el peso máximo del barco o el barco está ocupado.')
            # raise ContainerExcedePeso('El contenedor excede el peso máximo del barco o el barco está ocupado.')
    
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
        peso_total_containers = self.peso_containers()
        return len(self.containers) < self.max_container and peso_total_containers + container.peso <=self.max_peso


    
    #metodos para la segunda parte del tp
        
    def cargar_combustible(self, cantidad):
        self.combustible += cantidad
        if self.combustible > self.max_combustible:
            self.combustible = self.max_combustible

    def usarVela(self):
        if self.tiene_velas:
            self.usandoVela = True
            self.usandoMotor = False
        else:
            print("No tenes velas para usar")
    
    def usarMotor(self):
            self.usandoVela = False
            self.usandoMotor = True

    def obtener_tipo_dispositivo(self):
        if self.tiene_velas:
            return "Vela"
        else:
            return "Motor"

    def obtener_combustible_restante(self):
        return self.combustible
    
    def consumir_combustible(self, horas):
        if self.usandoVela:
            print("El barco esta usando velas.")
        else:
            print("El barco esta usando el motor.")
            self.consumo_combustible = horas * 6  # Consumo de combustible: 6L por hora
            if self.consumo_combustible > self.combustible:
                self.consumo_combustible = self.combustible  #el consumo no puede superar el combustible disponible
            self.combustible -= self.consumo_combustible
