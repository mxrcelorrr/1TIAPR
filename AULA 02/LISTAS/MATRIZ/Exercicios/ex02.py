matriz = [
    [1, 2],
    [3, 4]
]

escalar = 2

matriz_mult = []

for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        linha.append(matriz[i][j] * escalar)
    matriz_mult.append(linha)

print(matriz_mult)
