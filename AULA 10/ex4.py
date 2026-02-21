num1 = input(float("Digite o primeiro número: "))
num2 = input(float("Digite o segundo número: "))

try:
    resultado = num1 / num2
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Por favor, insira um número válido.")
else: 
    print("O resultado da divisão é:", resultado)   
    print("Operação concluída.")