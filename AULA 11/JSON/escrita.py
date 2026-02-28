import json

dados ={

}

caminho_arquivo = "novos_dados.json"

with open(caminho_arquivo, mode='w') as arquivo_json:
    json.dump(dados, arquivo_json, indent = 2)
print("Arquivo criado com sucesso")