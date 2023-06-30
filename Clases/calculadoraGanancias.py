from Empresa import empresa, Viaje

class CalculadoraGanancias:
    def __init__(self, barco):
        self.barco = barco

    def calcular_ganancias(self):
        ingresos = self.calcular_ingresos()
        gastos = self.calcular_gastos()
        ganancias = ingresos - gastos
        return ganancias

    def calcular_ingresos(self):
        ingresos = 0
        for Viaje in self.barco.viajesContenedor:
            ingresos += empresa.calcularPrecioEnvio(Viaje)
        return ingresos

    def calcular_gastos(self):
        consumo_combustible = self.barco.consumo_combustible
        gastos = consumo_combustible * self.barco.precioCombustible
        return gastos
