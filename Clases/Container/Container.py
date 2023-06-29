from abc import ABC

from Medidas import Medidas


class Container(ABC):
    def __init__(self, id, alto_int, ancho_int, ancho_ext, largo_int, alto_ext, largo_ext):
        self.__id = id
        self.__exterior = Medidas(ancho_ext, largo_ext, alto_ext)
        self.__interior = Medidas(ancho_int, largo_int, alto_int)
        self.__peso_max = 0
        self.__pies = 0
        self.__peso_actual = 0
        self.__max_vol = 0
        self.__vol = 0
        self.__cont_especial = False
        self.__completo = False

    # agregar getters y setters

    def set_cont_especial(self, especial):
        self.__cont_especial = especial

    def get_cont_especial(self):
        return self.__cont_especial

    def set_vol_maximo(self, valor):
        self.__max_vol = valor

    def get_vol_maximo(self):
        return self.__max_vol

    def set_espacio(self, carga):
        self.__vol += carga.get_volumen()
        self.__peso_actual += carga.get_peso()

    def set_peso_max(self, peso):
        self.__peso_max = peso

    def get_peso_max(self):
        return self.__peso_max

    def set_pies(self, pies):
        self.__pies = pies

    def get_pies(self):
        return self.__pies
    
    def estaCompleto(self):
        return self.__completo

    def getID(self):
        return self.__id
    
    def puedeSubir(self, Carga):
        #chequea si puede subir
        if self.estaCompleto() or Carga.peso > self.get_peso_max(): #falta chequear medidas
            return False
        
    def cargarContainer(self, Carga):
        #chequear si puede entrar la carga al contenedor
        if self.puedeSubir(self, Carga):
            #agregar la carga al container
            self._completo = True
