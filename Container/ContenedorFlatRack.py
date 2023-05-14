from TrabajoPracticoContainers.Container.Container import Container


class ContenedorFlatRack(Container):
    def __init__(self, id, tipo, peso, volumen, costo_base, costo_carga):
        super().__init__(id, tipo, peso, volumen, costo_base, costo_carga)
