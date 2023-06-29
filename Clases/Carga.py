from .Medidas import Medidas

class Carga:
    def __init__(self, id, peso, ancho, largo, alto, volumen, tipo):
        self.__id = id
        self.__peso = peso
        self.__medidas = Medidas(ancho, largo, alto)
        self.__carga_especial = False
        self.__volumen = volumen
        self.__tipo = tipo

    def set_medidas(self, ancho, largo, alto):
        self.__medidas.set_ancho(ancho)
        self.__medidas.set_largo(largo)
        self.__medidas.set_alto(alto)

    def get_carga_esp(self):
        return self.__carga_especial

    def set_carga_esp(self, especial):
        self.__carga_especial = especial

    def get_id(self):
        return self.__id

    def get_peso(self):
        return self.__peso

    def get_volumen(self):
        return self.__volumen

    def get_medidas(self):
        return self.__medidas
        
    def get_tipo(self): #puede ser alimenticia, química, maquinaria
        return self.__tipo
