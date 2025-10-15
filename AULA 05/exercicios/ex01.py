texto = input("Digite um arquivo txt ")

with open (texto, "r") as file:
    leitura = file.read()
    print(leitura)
    for palavra in leitura:
        print(palavra)