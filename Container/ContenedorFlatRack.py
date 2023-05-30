from Container.Container import Container


class ContenedorFlatRack(Container):
    def __init__(self, id):
        super().__init__(id, 2.3, None, None, 6.1, 2.3, 2.3)
        self.set_vol_maximo(33)
        self.set_peso_max(45000)
        self.set_cont_especial(True)
