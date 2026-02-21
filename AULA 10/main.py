try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado é: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
finally:
    print("Bloco finally executado.")