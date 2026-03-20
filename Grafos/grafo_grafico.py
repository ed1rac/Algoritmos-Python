import networkx as nx
import matplotlib.pyplot as plt

# Crie um grafo vazio
G = nx.Graph()

# Adicione vértices (nós)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

# Adicione arestas (conexões entre nós)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(1, 4)
G.add_edge(3, 1)

# Desenhe o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
plt.show()
