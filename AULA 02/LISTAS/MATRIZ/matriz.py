matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nova_linha = [10, 11, 12]
matriz.append(nova_linha)

#inserir
matriz[0].insert(0,100)

#remover coluna
elemento = matriz[0].pop(2)
print("\nElemento removido:", elemento)

#remover linha
del matriz[1]

print("Matriz após a remoção da segunda linha: ")
for linha in matriz:
    print(linha)

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()
