def mult(a, b):
    return a * b

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        return "erro: divisao por zero"
    return a / b

multiplicacao = mult(5, 7)
divisao = div(8, 7)
soma = sum(7, 10)
subtracao = sub(6, 7)

print(multiplicacao)
print(divisao)
print(soma)
print(subtracao)