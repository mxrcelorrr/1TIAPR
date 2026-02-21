texto = input("Digite um arquivo txt ")

try:  
    with open (texto, "r") as file:
        leitura = file.readlines()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o nome do arquivo e tente novamente.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um nome de arquivo válido.")
else:
    print(len(leitura))