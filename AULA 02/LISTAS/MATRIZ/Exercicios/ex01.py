matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_soma = []

for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        linha.append(matriz[i][j] + matriz1[i][j])
    matriz_soma.append(linha)

for linha in matriz_soma:
    for elemento in linha:
        print(f"{elemento:4}", end='')
    print()