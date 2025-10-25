texto = input("Digite um arquivo txt ")

with open (texto, "r") as file:
    leitura = file.read()
    print(leitura)
    palavra = leitura.split()
    print(len(palavra))