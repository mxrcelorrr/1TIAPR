import csv

caminho_arquivo = "novo_exemplo.csv"

dados = [
    ["Nome","Idade","Profissão","Cidade","País"],
    ["João","30","Engenheiro","São Paulo","Brasil"],
    ["Maria","25","Médica","Lisboa","Portugal"],
    ["Carlos","40","Professor","Madrid","Espanha"],
    ["Ana","35","Arquiteta","Paris","França"]
]

with open(caminho_arquivo, mode='r', newline='',encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

for linha in dados:
    