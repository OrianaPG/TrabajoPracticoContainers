from unittest import TestCase
from unittest.mock import Mock

from ..Clases.Barcos.Basico import Basico
# from Clases.Container.ContenedorBasico import ContenedorBasico
# from Clases.MockObj.GPSMock import GPSMock

class TestBarcos(TestCase):
    def test_obtener_distancia_recorrida(self):
        gps = Mock() #creo el mock

        gps.distancia.return_value = 150 #valor inventdo 

        # TODO: Crear función en Barco que "calcule" la distancia recorrida
        distancia = Basico.get_distancia(gps, "sede1", "sede2") # "calcula" la distancia

        self.assertEqual(distancia, 150) # chequea el resultado