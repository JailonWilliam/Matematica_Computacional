from mip import Model, xsum, minimize, BINARY, LinExpr

m = Model("Avaliação prática - Parte 4")

# Variáveis do modelo
X = [m.add_var(name='x', var_type=BINARY) for k in range(4)]
Y = [m.add_var(name='y', var_type=BINARY) for k in range(4)]

custo_fabric = [2.55, 2.47, 4.40, 1.90]
custo_comp = [3.10, 2.60, 4.50, 2.25]

maquina_A = [0.04, 0.00, 0.02, 0.06]
maquina_B = [0.02, 0.01, 0.06, 0.04]
maquina_C = [0.02, 0.05, 0.00, 0.15]
maquina_D = [0.00, 0.15, 0.06, 0.00]
maquina_E = [0.03, 0.09, 0.20, 0.00]
maquina_F = [0.06, 0.06, 0.20, 0.05]

maquinas = [maquina_A, maquina_B, maquina_C, maquina_D, maquina_E, maquina_F]

# Função objetivo
m.objective = minimize(150*xsum(custo_fabric[i]*X[i] + custo_comp[i]*Y[i] for i in range(4)))
   
#    2.55*X[0] + 2.47*X[1] + 4.40*X[2] + 1.90*X[3] + 3.10*Y[0] + 2.60*Y[1] + 4.50*Y[2] + 2.25*Y[3]))

# Restrição: O item produzido não será comprado e vice-versa
for i in range(4):
    m += X[i] + Y[i] == 1


# Ideia para o laço abaixo 
# m += 150*xsum(maquina_A[k]*X[k] for k in range(len(maquina_A))) <= 40

# Restrição: tempo das máquinas A, ..., F
for maq in maquinas:
     m += 150*xsum(maq[k]*X[k] for k in range(len(maq))) <= 40
   
# m += 150*(0.04*X[0] + 0.00*X[1] + 0.02*X[2] + 0.06*X[3]) <= 40 #A
# m += 150*(0.02*X[0] + 0.01*X[1] + 0.06*X[2] + 0.04*X[3]) <= 40 #B
# m += 150*(0.02*X[0] + 0.05*X[1] + 0.00*X[2] + 0.15*X[3]) <= 40 #C
# m += 150*(0.00*X[0] + 0.15*X[1] + 0.06*X[2] + 0.00*X[3]) <= 40 #D
# m += 150*(0.03*X[0] + 0.09*X[1] + 0.20*X[2] + 0.00*X[3]) <= 40 #E
# m += 150*(0.06*X[0] + 0.06*X[1] + 0.20*X[2] + 0.05*X[3]) <= 40 #F

m.optimize()

# Imprimir a solução
print("Função objetivo:", m.objective_value)

comp_comprados = ''
comp_produzidos = ''

for i in range(4):
    if(X[i].x == 1.0):
     comp_comprados += f'{i+1}, '
             
print(f"Componentes comprados: {comp_comprados[:-2]}")

for i in range(4):
    if(Y[i].x == 1.0):
     comp_produzidos += f'{i+1}, '

print(f"Componentes produzidos: {comp_produzidos[:-2]}")
