lista = ["bell", "arai", "schulberth", "stilo"]

try:
    indice = int(input("Digite um índice para acessar a lista: "))
    print(f"O elemento no índice {indice} é: {lista[indice]}")
except IndexError:
    print("Erro: Índice fora do intervalo. Verifique o índice e tente novamente.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
finally:
    print("Bloco finally executado.")