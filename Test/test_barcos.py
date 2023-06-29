from unittest import TestCase
from unittest.mock import Mock

from ..Clases.Barcos.Basico import Basico

class TestBarcos(TestCase):
    def test_obtener_distancia_recorrida(self):
        barco = Basico(1, 3, 250)
        gps = Mock()
        gps.calcularDistancia.return_value = 100
        distancia = gps.calcularDistancia(barco.get_sede_inicio, barco.get_sede_fin)
        barco.set_distancia = distancia
        self.assertEqual(distancia, 100)

    def test_obtener_tiempo_viaje(self):
        barco = Basico(2, 3, 250)
        gps = Mock()
        gps.calcularTiempoEnHoras.return_value = 2
        tiempo = gps.calcularTiempoEnHoras(barco.get_sede_inicio, barco.get_sede_fin)
        self.assertEqual(tiempo, 2)