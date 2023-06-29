from ..Container.Container import Container

class ContenedorBasicoHC(Container):
    def __init__(self, id):
        super().__init__(id, 230, 235, 245, 120, 260, 121)
        self.set_peso_max(32500)
        self.set_vol_maximo(67.7)
        self.set_pies(40)

    def get_peso_max(self):
        return super().get_peso_max()
    
    def puedeSubir(self, Carga):
        #chequea si puede subir
        if self.estaCompleto() or Carga.get_peso() > self.get_peso_max() or Carga.get_tipo() == "alimenticia": #falta chequear medidas
            return False
        
    def cargarContainer(self, Carga):
        #chequear si puede entrar la carga al contenedor
        if self.puedeSubir(Carga):
            #agregar la carga al container
            self._completo = True 
