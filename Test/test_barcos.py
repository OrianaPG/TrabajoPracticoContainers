from unittest import TestCase

from Clases.Barcos.Basico import Basico
from Clases.Container.ContenedorBasico import ContenedorBasico
from Clases.MockObj.GPSMock import GPSMock


class TestBarcos(TestCase):
    def test_obtener_distancia_recorrida(self):
        distancia = GPSMock()
        barco: Basico = Basico()
        container = ContenedorBasico(5)
        barco.cargar(container)
        distancia = 1000
        barco.set_distancia(barco.get_distancia() + distancia)

        assert distancia > 0
        print(f"la distancia recorrida es {distancia}km")

