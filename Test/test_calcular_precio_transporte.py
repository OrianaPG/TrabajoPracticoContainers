from unittest import TestCase

from Clases.Barcos.Basico import Basico
from Clases.Container.ContenedorBasico import ContenedorBasico
from Clases.Container.Container import Container
from Clases.Carga import Carga

def test_calcular_precio_transporte():
    #retira container en el puerto
    distancia = 80 
    contenedor_completo = True
    carga = Carga(peso=500, volumen=2.5)
    precio_esperado = 200000
    assert Container.calcular_costo_total(distancia, contenedor_completo, carga) == precio_esperado

    #puerta a puerta
    distancia = 1200 
    contenedor_completo = False
    carga = Carga(peso=800, volumen=3.2)
    precio_esperado = 1200 + (800 // 100 * 1100)  # 1200 + 8800 = 10000
    assert Container.calcular_costo_total(distancia, contenedor_completo, carga) == precio_esperado

    # container completo
    distancia = 8500 
    contenedor_completo = True
    carga = Carga(peso=2000, volumen=8.5)
    precio_esperado = 230000
    assert Container.calcular_costo_total(distancia, contenedor_completo, carga) == precio_esperado

    # usa prte del container
    distancia = 15000  
    contenedor_completo = False
    carga = Carga(peso=500, volumen=2)
    precio_esperado = 1500 + (500 // 100 * 1500)  # 1500 + 7500 = 9000
    assert Container.calcular_costo_total(distancia, contenedor_completo, carga) == precio_esperado