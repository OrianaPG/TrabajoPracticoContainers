from Medidas import Medidas


class Container:
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
        self.__espacio = False

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

    """def calcular_costo_total(self, distancia, container_completo):
        if container_completo:
            precio = self.costo_base
        else:
            pass
        if distancia < 100:
            precio += 200000
        elif distancia < 1000:
            precio += 210000
        elif distancia < 10000:
            precio += 230000
        else:
            precio += 250000
        return precio
    """
