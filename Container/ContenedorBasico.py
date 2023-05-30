from Container.Container import Container


class ContenedorBasico(Container):
    def __init__(self, id):
        super().__init__(id, 230, 235, 245, 600, 260, 610)
        self.set_vol_maximo(32.6)
        self.set_peso_max(24000)
