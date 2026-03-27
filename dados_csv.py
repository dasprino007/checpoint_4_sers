from csv import writer
from datetime import timedelta

def MiB_to_mb(mib: float):
    return mib * 1.048576

def formatar_tempo(td:timedelta):
    total_tempo = td.total_seconds()
    return f"{total_tempo}"

def salvar_dados_memoria_csv(nome_arquivo: str,insercao: float, busca: float, remocao: float):
    dados = [
        ["nome", "uso_maximo_memoria"],
        ["insercao", MiB_to_mb(insercao)],
        ["busca",    MiB_to_mb(busca)],
        ["remocao",  MiB_to_mb(remocao)],
    ]

    with open(f"data/{nome_arquivo}_memoria.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = writer(arquivo) # cria um objeto escritor
        escritor.writerows(dados)

def salvar_dados_tempo_csv(nome_arquivo: str,insercao: timedelta, busca: timedelta, remocao: timedelta):
    dados = [
        ["nome", "tempo_de_execucao"],
        ["insercao", formatar_tempo(insercao)],
        ["busca",    formatar_tempo(busca)],
        ["remocao",  formatar_tempo(remocao)],
    ]

    with open(f"data/{nome_arquivo}_tempo_execucao.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = writer(arquivo) # cria um objeto escritor
        escritor.writerows(dados)