from mip import Model, xsum, maximize, BINARY

# Jailon William Bruno Oliveira da Silva - 499441
# Davi Monteiro Pedrosa Moreira Sales - 496314

# IMPLEMENTAÇÃO DA QUESTÃO 2.B)
# O GRAFO UTILIZADO COMO EXEMPLO PARA O ITEM B ESTÁ DESENHADO NO ARQUIVO.PDF

m = Model("Avaliação Prática - Questão 02")

# REPRESENTAÇÃO COMPUTACIONAL DO GRAFO
listaDeAdjacente = { #Lista de adjacencia do grafo da questao 2.b), grafo de petersen com pesos
    'A': ['B', 'F', 'E'],
    'B': ['A', 'G', 'C'],
    'C': ['B', 'D', 'H'],
    'D': ['C', 'E', 'I'],
    'E': ['A', 'J', 'D'],
    'F': ['A', 'G', 'J'],
    'G': ['B', 'F', 'H'],
    'H': ['C', 'G', 'I'],
    'I': ['D', 'H', 'J'],
    'J': ['F', 'E', 'I']
}

pesosVertice = { #Peso dos vértices do grafo
    'A': 17,
    'B': 21,
    'C': 12,
    'D': 8,
    'E': 15,
    'F': 11,
    'G': 9,
    'H': 23,
    'I': 20,
    'J': 14
}

# VARIAVEL DO MODELO

# OBS:
# 1. ListaDeADjacente.keys() pega apenas as chaves do dicionário, isto é, os vértices do grafo! (generalizando)
# 2. A ideia é que o X seja um Dicionário! ao acessarmos o valor do primeiro vértice, ele retorna o conteúdo, isto é, {0,1}! 

X = {vertice: m.add_var(var_type=BINARY) for vertice in listaDeAdjacente.keys()}
print(f"AQUI TEU X: {X}")

# FUNÇÃO OBJETIVO
m.objective = maximize(xsum(pesosVertice[vertice] * X[vertice] for vertice in listaDeAdjacente.keys()))

# RESTRIÇÃO: A soma do vértice com seus adjacentes tem que ser <= 1
for vertice in listaDeAdjacente:
    for verticeAdj in listaDeAdjacente[vertice]:
        m += X[vertice] + X[verticeAdj] <= 1

m.optimize()

# Printando os vértices escolhidos para o conjunto independente
print("Função Objetivo:", m.objective_value)

print("\nVértices escolhido:")
for i in listaDeAdjacente:
    if X[i].x == 1:
        print(f"Vértice: {i} -> Peso: {pesosVertice[i]}")

# Printando a visão geral da solução! :D
print("\nVisão Geral:")
for i in listaDeAdjacente:
    print(f"X[{i}].x: {X[i].x:}")
