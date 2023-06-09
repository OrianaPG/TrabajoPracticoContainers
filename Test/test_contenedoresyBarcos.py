from unittest import TestCase
from ..Clases.Empresa import Empresa
from ..Clases.Container.Container import Container
from ..Clases.Barcos.Barco import Barco
from ..Clases.Carga import Carga

class test_contenedoresyBarcos(TestCase):
    def test_encontrar_Container_mas_viajes_completo(self):
        empresa = Empresa()  # instancia de la clase cmpresa con containers de prueba
        # Agregar containeres de prueba a la empresa
        
        carga1 = Carga(1, 2500, 1, 3, 5, 20.5, 'Alimenticia')
        carga2 = Carga(2, 3500, 1, 3, 5, 20.5, 'Alimenticia')
        carga3 = Carga(3, 4500, 1, 3, 5, 20.5, 'Alimenticia')
        carga4 = Carga(4, 5500, 1, 3, 5, 20.5, 'Alimenticia')
        carga5 = Carga(5, 6500, 1, 3, 5, 20.5, 'Alimenticia')

        Container1 = Container('001', 1, 2, 1.8, 5, 1.2, 2, 'Alimenticia')
        Container2 = Container('002', 1, 2, 1.8, 5, 1.2, 2, 'Alimenticia')
        Container3 = Container('003', 1, 2, 1.8, 5, 1.2, 2, 'Alimenticia')
        Container4 = Container('004', 1, 2, 1.8, 5, 1.2, 2, 'Alimenticia')
        Container5 = Container('005', 1, 2, 1.8, 5, 1.2, 2, 'Alimenticia')

        barco1 = Barco('001', 5, 35000, 2500, False, 450)
        barco2 = Barco('002', 1, 100000, 2500, False, 450)
        barco3 = Barco('003', 10, 200000, 2500, False, 450)

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
        #! Tiene problemas cargando el container, con peso_containers de Barcos Basico
        #? Es necesaria esa subclase? Cambia alguna función según el tipo de barco?
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
        
        barco1 = Barco('001', 5, 35000, 2500, False, 450)
        barco2 = Barco('002', 1, 100000, 2500, False, 450)
        barco3 = Barco('003', 10, 200000, 2500, False, 450)
        
        empresa.agregarBarco(barco1)
        empresa.agregarBarco(barco2)
        empresa.agregarBarco(barco3)
        
        BarcoMayorDistancia = empresa.encontrarBarcoMayorDistancia()
        

        #! Devuelve siempre barco1, hay que chequear si está bien cargado
        self.assertEqual(BarcoMayorDistancia, barco3)  #verifica

    def test_encontrar_barco_menor_distancia(self):
        empresa = Empresa()  # Instancia de la clase Empresa con barcos de prueba
        # Agregar barcos de prueba a la empresa
        
        barco1 = Barco('001', 500, 35000, 2500, False, 450)
        barco2 = Barco('002', 1000, 100000, 2500, False, 450)
        barco3 = Barco('003', 2000, 200000, 2500, False, 450)
        
        empresa.agregarBarco(barco1)
        empresa.agregarBarco(barco2)
        empresa.agregarBarco(barco3)
        
        barcoMenorDistancia = empresa.encontrarBarcoMenorDistancia()
        
        self.assertEqual(barcoMenorDistancia, barco1)#verifica  
