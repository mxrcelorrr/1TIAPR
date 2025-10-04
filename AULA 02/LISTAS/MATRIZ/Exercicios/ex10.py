matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_diagonal_principal = 0
soma_diagonal_secundaria = 0

for i in range(len(matriz)):
    soma_diagonal_principal += matriz[i][i]
    soma_diagonal_secundaria += matriz[i][len(matriz) - 1- i]

print("soma da diagonal principal", soma_diagonal_principal)
print("soma da diagonal secundaria", soma_diagonal_secundaria)