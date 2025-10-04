matriz = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
]

simetria = True

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] != matriz[j][i]:
            simetria = False
            break
    if not simetria:
        break

if simetria:
    print("A matriz eh simetrica")
else:
    print("A matriz n eh simetrica")
