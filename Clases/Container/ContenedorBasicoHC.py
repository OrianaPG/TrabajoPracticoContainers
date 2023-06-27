from Container.Container import Container

class ConenedorBasicoHC(Container):
    def __init__(self, id):
        super().__init__(id, 230, 235, 245, 120, 260, 121)
        self.set_peso_max(32500)
        self.set_vol_maximo(67.7)
        self.set_pies(40)