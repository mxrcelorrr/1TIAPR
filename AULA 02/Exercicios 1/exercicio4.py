vogais = ["a", "e", "i", "o", "u"]

caracter = input("Digite um caractere: ")
if caracter in vogais:
    print(f"O caractere '{caracter}' eh uma vogal")
else:
    print(f"O caractere '{caracter}' nao eh uma vogal")