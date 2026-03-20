class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        self.adicionar_vertice(vertice1)
        self.adicionar_vertice(vertice2)
        self.adjacencia[vertice1].append(vertice2)
        self.adjacencia[vertice2].append(vertice1)

    def mostrar_grafo(self):
        for vertice, vizinhos in self.adjacencia.items():
            print(f'{vertice}: {vizinhos}')


grafo = Grafo()
grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('A', 'C')
grafo.adicionar_aresta('B', 'C')
grafo.adicionar_aresta('C', 'D')

grafo.mostrar_grafo()
