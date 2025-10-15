lista = ["maçã, banana, morango, melancia, uva"]

with open("frutas.txt", "w", encoding="UTF-8") as file:
    for fruta in lista:
        file.write(fruta + "\n")
