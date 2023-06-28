import unittest
from Empresa import Empresa
from Container import Container
from Barcos import Barco

class test_contenedoresyBarcos(unittest.TestCase):
    def test_encontrar_Container_mas_viajes_completo(self):
        empresa = Empresa()  # instancia de la clase cmpresa con containers de prueba
        # Agregar containeres de prueba a la empresa
        
        Container1 = Container('001', True)
        Container2 = Container('002', True)
        Container3 = Container('003', False)
        Container4 = Container('004', True)
        Container5 = Container('005', True)
        
        empresa.agregarContenedor(Container1)
        empresa.agregarContenedor(Container2)
        empresa.agregarContenedor(Container3)
        empresa.agregarContenedor(Container4)
        empresa.agregarContenedor(Container5)

        empresa.enviarContenedor(Container1)#falta aaclarar destino y origen
        empresa.enviarContenedor(Container5)
        empresa.enviarContenedor(Container3)
        empresa.enviarContenedor(Container1)
        empresa.enviarContenedor(Container2)

        
        ContenedorMasViajesCompleto = empresa.encontrarContenedorMasViajesCompleto()
        
        self.assertEqual(ContenedorMasViajesCompleto, '002') #verifica

    def test_encontrar_barco_mayor_distancia(self):
        empresa = Empresa()  # instancia de la clase Empresa con barcos de prueba
        # Agregar barcos de prueba a la empresa
        
        barco1 = Barco('001', 5, 35000)
        barco2 = Barco('002', 1, 100000)
        barco3 = Barco('003', 10, 200000)
        
        empresa.agregarBarco(barco1)
        empresa.agregarBarco(barco2)
        empresa.agregarBarco(barco3)
        
        BarcoMayorDistancia = empresa.encontrarBarcoMayorDistancia()
        
        self.assertEqual(BarcoMayorDistancia, barco3)  #verifica

    def test_encontrar_barco_menor_distancia(self):
        empresa = Empresa()  # Instancia de la clase Empresa con barcos de prueba
        # Agregar barcos de prueba a la empresa
        
        barco1 = Barco('001', 500)
        barco2 = Barco('002', 1000)
        barco3 = Barco('003', 2000)
        
        empresa.agregarBarco(barco1)
        empresa.agregarBarco(barco2)
        empresa.agregarBarco(barco3)
        
        barcoMenorDistancia = empresa.encontrarBarcoMenorDistancia()
        
        self.assertEqual(barcoMenorDistancia, barco1)#verifica  
