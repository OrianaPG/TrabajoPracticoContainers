import unittest
from Empresa import Empresa
from Container import Container
from Barcos import Barco

class test_contenedoresyBarcos(unittest.TestCase):
    def test_encontrar_Container_mas_viajes_completo(self):
       empresa = Empresa()  # instancia de la clase cmpresa con containers de prueba
        # Agregar containeres de prueba a la empresa
        
        carga1 = Carga()
        carga2 = Carga()
        carga3 = Carga()
        carga4 = Carga()
        carga5 = Carga()

        Container1 = Container('001')
        Container2 = Container('002')
        Container3 = Container('003')
        Container4 = Container('004')
        Container5 = Container('005')

        barco1 = Barco('001', 5, 35000)
        barco2 = Barco('002', 1, 100000)
        barco3 = Barco('003', 10, 200000)

        empresa.agregarBarco(barco1)
        empresa.agregarBarco(barco2)
        empresa.agregarBarco(barco3)
        
        empresa.agregarContenedor(Container1)
        empresa.agregarContenedor(Container2)
        empresa.agregarContenedor(Container3)
        empresa.agregarContenedor(Container4)
        empresa.agregarContenedor(Container5)

        Container1.cargarContainer(carga1)
        Container2.cargarContainer(carga2)
        Container3.cargarContainer(carga3)
        Container4.cargarContainer(carga4)

        barco1.cargar_container(Container1)
        barco2.cargar_container(Container3)
        barco3.cargar_container(Container2)

        empresa.enviar_barco(barco1)#falta aaclarar destino y origen
        
        Container1.cargarContainer(carga5)
        
        barco1.cargar_container(Container1)
        
        empresa.enviar_barco(barco1)
        empresa.enviar_barco(barco2)
        
        barco2.cargar_container(Container4)
    
        empresa.enviar_barco(barco2)
        empresa.enviar_barco(barco3)
        
        ContenedorMasViajesCompleto = empresa.encontrarContenedorMasViajesCompleto()
        
        self.assertEqual(ContenedorMasViajesCompleto, '001') #verifica

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
