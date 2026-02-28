import csv

caminho_arquivo = "exemplo.csv"

dados = [
    ["Nome","Idade","Profissão","Cidade","País"],
    ["João","30","Engenheiro","São Paulo","Brasil"],
    ["Maria","25","Médica","Lisboa","Portugal"],
    ["Carlos","40","Professor","Madrid","Espanha"],
    ["Ana","35","Arquiteta","Paris","França"]
]


with open(caminho_arquivo, mode='r', newline='',encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    matriz = list(arquivo_csv)
    linhas = len(matriz)
    colunas = len(matriz[0])
    print(colunas)
    print(linhas)
    
    for i in range(0, linhas):
        for j in range(0, colunas):
            print(f"| {matriz[i][j]} |", end="")


    for linha in leitor_csv:
        coluna1, coluna2, coluna3, coluna4, coluna5 = linha
        print(f"Coluna 1: {coluna1}, Coluna 2: {coluna2}, Coluna 3 {coluna3}, Coluna 4 {coluna4}, Coluna 5 {coluna5}")

