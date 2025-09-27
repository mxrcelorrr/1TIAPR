matriz = [
    [1, 0, 0]
    [0, 1, 0]
    [0, 0, 1]
]

n = len(matriz) #linha        
m = len(matriz[0])  #coluna

if n != m:
    print("Nao eh matriz")
else:
    identidade = True
    for i in range(n):
        for j in range(m):
            if i == j:
                if matriz[i][j] != 1:
                    identidade = False
            else:  
                if matriz[i][j] != 0:
                    identidade = False
    if identidade:
        print("É matriz identidade")
    else:
        print("Não é matriz identidade")