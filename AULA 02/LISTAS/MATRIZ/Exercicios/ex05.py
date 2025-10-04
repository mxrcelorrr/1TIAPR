matriz_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

linhas_a = len(matriz_a)
colunas_a = len(matriz_a[0])
linhas_b = len(matriz_b)
colunas_b = len(matriz_b[0])

if colunas_a != linhas_b:
    raise ValueError("numero de colunas da matriz 1 dever ser igual ao numero de linhas da matriz 2")

resultado = []

for i in range(linhas_a):
    linha_resultado = []
    for j in range(colunas_b):
        soma = 0
        for k in range(colunas_a):
            soma += matriz_a[i][j] * matriz_b[k][j]
        linha_resultado.append(soma)
    resultado.append(linha_resultado)

for linha in resultado:
    print(linha)