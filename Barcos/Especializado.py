from TrabajoPracticoContainers.Barcos.Barco import Barco


class Especializado(Barco):
    def __init__(self, id, max_container, max_peso):
        super().__init__(id, max_container, max_peso)
