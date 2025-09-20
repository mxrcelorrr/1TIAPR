acumulador = 0

num = int(input("Digite um numero: "))
while num >= 0:
    acumulador += num
    num = int(input("Digite um numero: "))
print(f"A soma dos numero eh: {acumulador}")