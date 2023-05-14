class Barco:
    def __init__(self, id, max_container, max_peso):
        self.id = id
        self.max_container = max_container
        self.max_peso = max_peso
        self.containers = []
        self.distancia_recorrida = 0

    def cargar_container(self, container):
        if len(self.containers) < self.max_container and self.max_peso >= sum(
                [cont.peso for cont in self.containers]) + container.peso:
            self.containers.append(container)

    def cantidad_containers(self):
        cantidad = 0
        for c in self.containers:
            cantidad = cantidad + 1
        return cantidad

    def peso_containers(self):
        peso_containers = 0
        for c in self.containers:
            peso_containers = peso_containers + c.peso
        return peso_containers
