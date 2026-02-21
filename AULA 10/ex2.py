try:
    texto = input("Digite um arquivo txt ")

    with open (texto, "r") as file:
        leitura = file.read()
        print(leitura)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o nome do arquivo e tente novamente.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um nome de arquivo válido.")
finally:
    print("Bloco finally executado.")
    