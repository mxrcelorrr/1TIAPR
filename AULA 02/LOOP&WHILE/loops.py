for x in range(100):
    print(x)

lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)

for letra in "Python":
    print(letra)

for numero in range(5, 15, 2):
    print(numero)
   
""" class range(
    start: SupportsIndex,
    stop: SupportsIndex,
    step: SupportsIndex,
) """

lista_num = [1, 2, 3, 4, 5]

resultado = 0
for num in lista_num:
    resultado += num
print(resultado)

while True:
    comando = input("Digite 'sair' para encerrar:")
    if comando == 'sair':
        break
    print("Você digitou:", comando)