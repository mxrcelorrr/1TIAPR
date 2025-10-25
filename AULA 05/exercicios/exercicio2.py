texto1 = input("Digite um arquivo txt ")
texto2 = input("Digite outro arquivo txt ")


with open(texto1, "r") as f1, open(texto2, "r") as f2:
    file1 = f1.read()
    file2 = f2.read()

with open("arquivo_combinado.txt", "w") as file3:
    file3.write(file1 + "\n" + file2)



    