from mip import Model, xsum, maximize, BINARY

# Jailon William Bruno Oliveira da Silva - 499441
# Davi Monteiro Pedrosa Moreira Sales - 496314

# IMPLEMENTAÇÃO DA QUESTÃO 2.A)

m = Model("Avaliação Prática - Questão 02")

listaDeAdjacente = { #Lista de adjacencia do grafo da questao 2.a)
    1: [2, 3],
    2: [1, 3, 4, 6],
    3: [1, 2, 6],
    4: [2, 5, 6],
    5: [4, 6],
    6: [3, 2, 4, 5]
}

pesosVertice = { #Peso dos vértices do grafo da questao 2.a)
    1: 5,
    2: 10,
    3: 10,
    4: 15,
    5: 20,
    6: 15
}

# VARIAVEL DO MODELO

# OBS:
# 1. ListaDeADjacente.keys() pega apenas as chaves do dicionário, isto é, os vértices do grafo! (generalizando)
# 2. A ideia é que o X seja um Dicionário! ao acessarmos o valor do primeiro vértice, ele retorna o conteúdo, isto é, {0,1}! 

X = {vertice: m.add_var(var_type=BINARY) for vertice in listaDeAdjacente.keys()}
print(f"AQUI TEU X: {X}")
# Função objetivo
m.objective = maximize(xsum(pesosVertice[vertice] * X[vertice] for vertice in listaDeAdjacente.keys()))

# Restrição: A soma do vértice com seus adjacentes tem que ser <= 1
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

print("\nVisão Geral:")
for i in listaDeAdjacente:
    print(f"X[{i}].x: {X[i].x:}")
