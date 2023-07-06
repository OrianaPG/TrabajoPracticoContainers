from unittest import TestCase

from ..Clases.Empresa import Empresa
from ..Clases.Carga import Carga
from ..Clases.Viaje import Viaje
from ..Clases.Container.Container import Container

class test_calcular_precio_transporte(TestCase):

    def test_retira_container_en_el_puerto(self):
        container = Container(1, 1, 2, 1.8, 5, 1.2, 2, 'Alimenticia')
        distancia = 80 
        viaje = Viaje(container, distancia, False)
        # peso = 500
        # tipo = 'Alimenticia'
        # carga = Carga(1, peso, 1, 3, 5, 20.5, tipo)
        precio_esperado = 200000
        empresa = Empresa()
        self.assertEqual(empresa.calcularPrecioEnvio(viaje), precio_esperado)

    def test_puerta_a_puerta(self):
        container = Container(2, 1, 2, 1.8, 5, 1.2, 2, 'Alimenticia')
        distancia = 1200 # menos de 10000
        viaje = Viaje(container, distancia, True)
        # contenedor_completo = False 
        # peso = 800
        # tipo = 'Alimenticia'
        # carga = Carga(2, peso, 1, 3, 5, 13.2, tipo)
        precio_esperado = 800 // 100 * 1150 + 20000 #29200, cada 1150 cada 100kg + precio del camion
        empresa = Empresa()
        self.assertEqual(empresa.calcularPrecioEnvio(viaje), precio_esperado)

    def test_container_completo(self):
        container = Container(3, 1, 2, 1.8, 5, 1.2, 2, 'Alimenticia')
        distancia = 8500 
        viaje = Viaje(container, distancia, False)
        # contenedor_completo = True
        # peso = 2000
        # tipo = 'Alimenticia'
        # carga = Carga(3, peso, 1, 3, 5, 18.5, tipo)
        precio_esperado = 230000
        empresa = Empresa()
        self.assertEqual(empresa.calcularPrecioEnvio(viaje), precio_esperado)

    def test_usa_parte_del_container(self):
        container = Container(4, 1, 2, 1.8, 5, 1.2, 2, 'Alimenticia')
        distancia = 15000
        viaje = Viaje(container, distancia, False)
        # contenedor_completo = False
        # peso = 500
        # tipo = 'Alimenticia'
        # carga = Carga(4, peso, 1, 3, 5, 20, tipo)
        precio_esperado = 500 // 100 * 1500 #7500, 1500 cda 100kg
        empresa = Empresa()
        self.assertEqual(empresa.calcularPrecioEnvio(viaje), precio_esperado)
