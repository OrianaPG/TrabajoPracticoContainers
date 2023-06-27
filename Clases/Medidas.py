class Medidas:
    def __init__(self, ancho, largo, alto):
        self.__ancho = ancho
        self.__largo = largo
        self.__alto = alto

    def get_largo(self):
        return self.__largo

    def set_largo(self, valor):
        self.__largo = valor

    def get_ancho(self):
        return self.__ancho

    def set_ancho(self, valor):
        self.__ancho = valor

    def get_alto(self):
        return self.__alto

    def set_alto(self, valor):
        self.__alto = valor


