import time
import itertools
import random
import networkx as nx
import matplotlib.pyplot as plt


# Função para gerar uma matriz de distâncias fixa
def matriz_distancias_fixa(num_cidades):
    base = 10  # Base inicial para os cálculos de distância
    matriz = [[0] * num_cidades for _ in range(num_cidades)]  # Inicializa matriz vazia

    for i in range(num_cidades):
        for j in range(i + 1, num_cidades):
            # Cálculo da distância: soma dos índices + 1, multiplicada por 5
            distancia = (i + j + 1) * 5
            matriz[i][j] = distancia
            matriz[j][i] = distancia

    return matriz


# Função para gerar uma matriz de distâncias com valores aleatórios
def matriz_distancias_aleatoria(num_cidades):
    matriz = [[0] * num_cidades for _ in range(num_cidades)]
    for i in range(num_cidades):
        for j in range(i + 1, num_cidades):
            distancia = random.randint(1, 100)
            matriz[i][j] = distancia
            matriz[j][i] = distancia
    return matriz


def imprimir_matriz(distancias):
    num_cidades = len(distancias)

    print(f"Matriz de distâncias para {num_cidades} cidades:")

    # Encontrar o comprimento máximo dos valores para formatação
    max_tamanho = max(len(str(distancias[i][j])) for i in range(num_cidades) for j in range(num_cidades))

    # Criar o cabeçalho horizontal
    cabecalho_horizontal = " " * (max_tamanho + 1)  # Espaço inicial para o cabeçalho vertical
    for i in range(num_cidades):
        cabecalho_horizontal += f"{chr(65 + i).ljust(max_tamanho)} "  # Adiciona a letra correspondente à cidade com alinhamento
    print(cabecalho_horizontal)

    # Criar o cabeçalho vertical e imprimir a matriz
    for i in range(num_cidades):
        linha = f"{chr(65 + i).ljust(max_tamanho)} "  # Adiciona a letra correspondente à cidade na coluna vertical com alinhamento
        for j in range(num_cidades):
            linha += f"{str(distancias[i][j]).ljust(max_tamanho)} "  # Adiciona o valor da matriz com alinhamento
        print(linha)


# Função que calcula a distância total de uma rota específica
def calcular_distancia(rota):
    distancia_total = 0
    for i in range(len(rota) - 1):
        distancia_total += distancias[rota[i]][rota[i + 1]]
    distancia_total += distancias[rota[-1]][rota[0]]  # Volta à cidade de origem
    return distancia_total


# Função que converte rota de números para letras e formata com vírgulas
def converter_rota_para_letras(rota):
    return ', '.join(chr(65 + cidade) for cidade in rota)


# Exibir a melhor rota de forma mais amigável
def exibir_melhor_rota(melhor_rota):
    return ' -> '.join(melhor_rota.split(', '))


# Simulação do problema do caixeiro viajante usando força bruta
def caixeiro_viajante():
    cidades = list(range(len(distancias)))
    menor_distancia = float('inf')
    melhor_rota = None

    # Permutação de todas as possíveis rotas
    for rota in itertools.permutations(cidades):
        distancia = calcular_distancia(rota)
        rota_letras = converter_rota_para_letras(rota)
        # Exibe a rota atual e sua distância
        if distancia < menor_distancia:
            menor_distancia = distancia
            melhor_rota = rota_letras
            print(f"Rota: {rota_letras} | Distância: {distancia} <- Menor até agora")
        else:
            print(f"Rota: {rota_letras} | Distância: {distancia}")

    return melhor_rota, menor_distancia


def exibir_grafo(distancias, melhor_rota=None):
    G = nx.Graph()

    # Adiciona as arestas ao grafo com as distâncias como peso
    num_cidades = len(distancias)
    for i in range(num_cidades):
        for j in range(i + 1, num_cidades):
            G.add_edge(chr(65 + i), chr(65 + j), weight=distancias[i][j])

    pos = nx.spring_layout(G)  # Layout do grafo

    # Desenhar o grafo
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_color='black',
            edge_color='gray')

    # Adiciona os pesos das arestas
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Se existir uma melhor rota, destaque-a
    if melhor_rota:
        rota_nos = [chr(65 + int(ord(c) - 65)) for c in melhor_rota.split(", ")]
        edges = [(rota_nos[i], rota_nos[i + 1]) for i in range(len(rota_nos) - 1)]
        edges.append((rota_nos[-1], rota_nos[0]))  # Volta à cidade de origem
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='blue', width=2)

    plt.show()


def menu():
    global distancias
    print("Escolha o método de geração da matriz de distâncias:")
    print("1. Fixa")
    print("2. Aleatória")

    escolha = input("Digite o número da opção desejada: ")

    if escolha not in ['1', '2']:
        print("Opção inválida.")
        return

    num_cidades = int(input("Digite o número de cidades (3, 5, 6, 7, 8, 10): "))
    if escolha == '1':
        if num_cidades in [3, 5, 6, 7, 8, 10]:
            distancias = matriz_distancias_fixa(num_cidades)
        else:
            print("Número de cidades não suportado para a matriz fixa.")
            return
    elif escolha == '2':
        distancias = matriz_distancias_aleatoria(num_cidades)

    print()
    imprimir_matriz(distancias)

    # Exibe o grafo da matriz de distâncias
    print("\nExibindo o grafo da matriz de distâncias:")
    exibir_grafo(distancias)

    tempo_inicio = time.time()
    melhor_rota, menor_distancia = caixeiro_viajante()
    tempo_total = time.time() - tempo_inicio
    print()
    imprimir_matriz(distancias)
    print()
    print("\nMelhor rota final: ", exibir_melhor_rota(melhor_rota))
    print("Menor distância final: ", menor_distancia)
    print(f"Tempo total de execução: {tempo_total:.2f} segundos.")

    # Exibe o grafo destacando a melhor rota
    print("\nExibindo o grafo com a melhor rota:")
    exibir_grafo(distancias, melhor_rota)


if __name__ == "__main__":
    menu()
