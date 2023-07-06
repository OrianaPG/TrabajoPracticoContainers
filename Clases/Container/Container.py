# from abc import ABC

from ..Medidas import Medidas
from ..Excepciones import CargaExcedeContainer, ContainerCompleto
from ..Carga import Carga

class Container():
    def __init__(self, id, alto_int, ancho_int, ancho_ext, largo_int, alto_ext, largo_ext,tipo):
        self.__id = id
        self.__medidas_ext = Medidas(ancho_ext, largo_ext, alto_ext)
        self.__medidas_int = Medidas(ancho_int, largo_int, alto_int)
        self.__peso_max = 0
        self.__pies = 0
        self.__peso_actual = 0
        self.__max_vol = 0
        self.__vol = 0
        self.__cont_especial = False
        self.__completo = False
        self.tipo = tipo

    def get_medidas_ext(self):
        return self.__medidas_ext
    
    def get_medidas_int(self):
        return self.__medidas_int

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

    def get_peso_actual(self):
        return self.__peso_actual
    
    def set_peso_actual(self, peso):
        self.__peso_actual += peso

    def set_pies(self, pies):
        self.__pies = pies

    def get_pies(self):
        return self.__pies
    
    def estaCompleto(self):
        return self.__completo

    def getID(self):
        return self.__id
    
    def puedeSubir(self, carga: Carga):
        #chequea si puede subir
        if self.estaCompleto():
            raise ContainerCompleto('El container está completo')
        else:
            if (self.get_peso_actual() + carga.get_peso()) > self.get_peso_max() and carga.get_medidas > self.get_medidas_int:
                raise CargaExcedeContainer('La carga excede las dimensiones o el peso del container')
            else:
                return True
        
    def cargarContainer(self, carga: Carga):
        #chequear si puede entrar la carga al contenedor
        if self.puedeSubir(carga):
            self.subirCargaAlContiner(carga)
            
    def subirCargaAlContiner(self, carga: Carga):
        self.__carga.append(carga)
        self.set_peso_actual(carga.get_peso())
        if self.get_peso_actual() == self.get_peso_max():
            self.estaCompleto = True
        
        
    def descargar(self):
        self.__carga.clear()
        self.set_peso_actual(0)
