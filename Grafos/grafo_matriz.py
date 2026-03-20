class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]

    def adicionar_aresta(self, vertice1, vertice2):
        self.matriz_adjacencia[vertice1][vertice2] = 1
        self.matriz_adjacencia[vertice2][vertice1] = 1

    def mostrar_grafo(self):
        for linha in self.matriz_adjacencia:
            print(linha)


grafo = Grafo(4)
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 2)
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(2, 3)

grafo.mostrar_grafo()
