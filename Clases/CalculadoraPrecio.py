class CalculadoraPrecio():
    
    def calcular_costo_total(self, distancia, container_completo, peso):
        if distancia < 100:
            if container_completo:
                precio = 200000
            else:
                precio = (peso // 100) * 1000
        elif distancia < 1000:
            if container_completo:
                precio = 210000
            else:
                precio = (peso // 100) * 1100
        elif distancia < 10000:
            if container_completo:
                precio = 230000
            else:
                precio = (peso // 100) * 1150
        else:
            if container_completo:
                precio = 250000
            else:
                precio = (peso // 100) * 1500

        return precio
