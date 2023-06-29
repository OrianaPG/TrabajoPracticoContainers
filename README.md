# Trabajo Práctico "Containers"  - Grupo 1

## Integrantes

- Graña, María Sol
- Pierucci Gandini, Oriana

## To do

- [x] Cambiar nombre excepción ContainerExcedePeso()
- [x] Crear excepción de CargaExcedeContainer
- [x] Hacer más legible la función cargar_container de Barco
- [x] Actualizar el diagrama de clases con todas las funciones
- [ ] Crear función que "calcule" la distancia recorrida (Mock, barco)

## Introducción

Una empresa que se dedica al transporte de containers desea desarrollar una aplicación que le permita gestionar su negocio. La empresa cuenta con una flota de barcos y camiones que le permiten transportar los mencionados containers entre distintos paises donde la empresa posee sedes.

### Reglas de negocio

1. Un barco no puede cargar más containers del máximo definido.
2. Un barco no puede cargar más peso del máximo definido.
3. Un barco no puede cargar un container para el cual no fue diseñado.
4. Un container con material especial (explosivos, desechos químicos o radioactivos) sólo puede ser transportado por un barco diseñado para tal fin.
5. Cualquier carga cuyas dimensiones, volumen o peso supere lo definido en el container no podrá ser trasladada en el mismo.

## Requisitos

Desarrollar una aplicación que permita emular la situación planteada y su solución, permitiendo obtener:

1. El precio que debe pagar un cliente por enviar una carga. Plantear distintos escenarios, por ejemplo:
    - Cliente retira la carga en el puerto.
    - Cliente contrata servicio puerta a puerta.
    - Utiliza container completo.
    - Utiliza sólo una porción del container.
2. El container que mayor cantidad de veces viajó completo con una única carga.
3. El barco que recorrió la mayor cantidad de Km.
4. El barco que recorrió la menor cantidad de Km.

La aplicación debe contar con un set de pruebas unitarias que permitan validar la ejecución de la misma.
Además de los planteados, deben agregarse otros casos, como los que fallan por no cumplir alguna regla de negocio.
