from ..Container.Container import Container

class ContenedorBasico(Container):
    def __init__(self, id):
        super().__init__(id, 230, 235, 245, 600, 260, 610)
        self.set_vol_maximo(32.6)
        self.set_peso_max(24000)
        self.set_pies(20)

    def get_peso_max(self):
        return self.__peso_max
    
    def puedeSubir(self, Carga):
        #chequea si puede subir
        if self.estaCompleto() or Carga.get_peso() > self.get_peso_max() or Carga.get_tipo() == "alimenticia": #falta chequear medidas
            return False
        
    def cargarContainer(self, Carga):
        #chequear si puede entrar la carga al contenedor
        if self.puedeSubir(self, Carga):
            #agregar la carga al container
            self._completo = True
