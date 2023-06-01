class Camion:
    def __init__(self, id):
        self.__id = id
        self.__cont = None
        self.__precio = 20000
        self.__cargado = False

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_cont(self):
        return self.__cont

    def set_cont(self, cont):
        self.__cont = cont

    def get_cargado(self):
        return self.__cargado

    def set_cargado(self, cargado):
        self.__cargado = cargado
