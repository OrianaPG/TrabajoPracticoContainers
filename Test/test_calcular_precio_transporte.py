from unittest import TestCase

# from ..Clases.Barcos.Basico import Basico
# from ..Clases.Container.ContenedorBasico import ContenedorBasico
from ..Clases.CalculadoraPrecio import CalculadoraPrecio
from ..Clases.Carga import Carga

class test_calcular_precio_transporte(TestCase):

    def test_retira_container_en_el_puerto(self):
        calculadora = CalculadoraPrecio()
        distancia = 80 
        contenedor_completo = True
        peso = 500
        carga = Carga(1, peso, 1, 3, 5, 20.5)
        precio_esperado = 200000
        assert calculadora.calcular_costo_total(distancia, contenedor_completo, carga.get_peso()) == precio_esperado

    def test_puerta_a_puerta(self):
        calculadora = CalculadoraPrecio()
        distancia = 1200 # menos de 10000
        contenedor_completo = False 
        peso= 800
        carga = Carga(2, peso, 1, 3, 5, 13.2)
        precio_esperado = 800 // 100 * 1150 #9200, cada 1150 cada 100kg
        assert calculadora.calcular_costo_total(distancia, contenedor_completo, carga.get_peso()) == precio_esperado

    def test_container_completo(self):
        calculadora = CalculadoraPrecio()
        distancia = 8500 
        contenedor_completo = True
        peso= 2000
        carga = Carga(3, peso, 1, 3, 5, 18.5)
        precio_esperado = 230000
        assert calculadora.calcular_costo_total(distancia, contenedor_completo, carga.get_peso()) == precio_esperado

    def test_usa_parte_del_container(self):
        calculadora = CalculadoraPrecio()
        distancia = 15000  
        contenedor_completo = False
        peso= 500
        carga = Carga(4, peso, 1, 3, 5, 20)
        precio_esperado = 500 // 100 * 1500 #7500, 1500 cda 100kg
        assert calculadora.calcular_costo_total(distancia, contenedor_completo, carga.get_peso()) == precio_esperado

