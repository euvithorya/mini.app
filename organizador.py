import json
from datetime import datetime

ARQUIVO_DADOS = "compromissos.json"

def carregar_compromissos():
    try:
        with open(ARQUIVO_DADOS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_compromissos(compromissos):
    with open(ARQUIVO_DADOS, "w") as arquivo:
        json.dump(compromissos, arquivo, indent=4)

def adicionar_compromisso(data, descricao):
    compromissos = carregar_compromissos()
    novo_compromisso = {"data": data, "descricao": descricao}
    compromissos.append(novo_compromisso)
    salvar_compromissos(compromissos)
    return "Compromisso adicionado com sucesso!"

def listar_compromissos():
    compromissos = carregar_compromissos()
    if not compromissos:
        return "Nenhum compromisso cadastrado."
    return "\n".join([f"{c['data']}: {c['descricao']}" for c in compromissos])

def buscar_compromissos_por_data(data):
    compromissos = carregar_compromissos()
    resultados = [c for c in compromissos if c["data"] == data]
    if not resultados:
        return "Nenhum compromisso encontrado para essa data."
    return "\n".join([f"{c['data']}: {c['descricao']}" for c in resultados])
