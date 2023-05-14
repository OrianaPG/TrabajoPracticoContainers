class Container:
    def __init__(self, id, tipo, peso, volumen, costo_base, costo_carga):
        self.id = id
        self.tipo = tipo
        self.peso = peso
        self.volumen = volumen
        self.costo_base = costo_base
        self.costo_carga = costo_carga

    def calcular_costo_total(self, distancia, container_completo):
        if container_completo:
            precio = self.costo_base
        else:
            pass
        if distancia < 100:
            precio += 200000
        elif distancia < 1000:
            precio += 210000
        elif distancia < 10000:
            precio += 230000
        else:
            precio += 250000
        return precio
