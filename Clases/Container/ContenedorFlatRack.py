from ..Container.Container import Container

class ContenedorFlatRack(Container):
    def __init__(self, id):
        super().__init__(id, 2.3, None, None, 6.1, 2.3, 2.3)
        self.set_vol_maximo(33)
        self.set_peso_max(45000)
        self.set_cont_especial(True)

    def get_peso_max(self):
        return super().get_peso_max()
    
    def puedeSubir(self, Carga):
        #chequea si puede subir
        if self.estaCompleto() or Carga.get_peso() > self.get_peso_max() or Carga.get_tipo() == "alimenticia": #falta chequear medidas
            return False
        else:
            return True
        
    def cargarContainer(self, Carga):
        #chequear si puede entrar la carga al contenedor
        if self.puedeSubir(self, Carga):
            #agregar la carga al container
            self._completo = True 
