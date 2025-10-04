matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]

transposta = []

for j in range(len(matriz[0])):
    linha = []
    for i in range(len(matriz)):
        linha.append(matriz[i][j])
    transposta.append(linha)

for linha in transposta:
    print (linha)