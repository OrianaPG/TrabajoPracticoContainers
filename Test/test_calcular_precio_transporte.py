from unittest import TestCase

from Barcos.Basico import Basico
from Container.ContenedorBasico import ContenedorBasico
from Container.CalculadoraPrecio import calcular_costo_total
from Carga import Carga

def test_calcular_precio_transporte():
    #retira container en el puerto
    distancia = 80 
    contenedor_completo = True
    carga = Carga(peso= 500, volumen=2.5)
    precio_esperado = 200000
    assert calcular_costo_total(distancia, contenedor_completo, carga) == precio_esperado

    #puerta a puerta
    distancia = 1200 # menos de 10000
    contenedor_completo = False 
    carga = Carga(peso= 800, volumen=3.2)
    precio_esperado = 800 // 100 * 1150 #9200, cada 1150 cada 100kg
    assert calcular_costo_total(distancia, contenedor_completo, carga) == precio_esperado

    # container completo
    distancia = 8500 
    contenedor_completo = True
    carga = Carga(peso= 2000, volumen=8.5)
    precio_esperado = 230000
    assert calcular_costo_total(distancia, contenedor_completo, carga) == precio_esperado

    # usa prte del container
    distancia = 15000  
    contenedor_completo = False
    carga = Carga(peso= 500, volumen=2)
    precio_esperado = 500 // 100 * 1500 #7500, 1500 cda 100kg
    assert calcular_costo_total(distancia, contenedor_completo, carga) == precio_esperado
