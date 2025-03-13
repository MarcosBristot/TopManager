import json

def carregar_dados(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)