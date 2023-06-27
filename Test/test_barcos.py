from unittest import TestCase

from Clases.Barcos.Basico import Basico
from Clases.Container.ContenedorBasico import ContenedorBasico
from Clases.MockObj.GPSMock import GPSMock

class TestBarcos(TestCase):
    def test_obtener_distancia_recorrida(self):
        gps = GPSMock() #creo el mock

        gps.distancia = GPSMock(return_value = 150) #valor inventdo 

        distancia = distancia(gps, "sede1", "sede2") # "calcula" la distancia

        self.assertEqual(distancia, 150) # chequea el resultado