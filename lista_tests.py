import random
import memory_profiler
import consts
from datetime import datetime, timedelta
from pyJoules.energy_meter import EnergyContext
from pyJoules.handler.csv_handler import CSVHandler
from dados_csv import salvar_dados_memoria_csv, salvar_dados_tempo_csv

def insercoes_lista(lista : list, qnt : int):
    for i in range(qnt):
        lista.append(i)

def remocoes_lista(lista : list, qnt : int):
    for i in range(qnt):
        lista.remove(i) # tenta remover o numero

def busca_lista(lista : list, qnt : int):
    for i in range(qnt):
        num = random.randint(1,len(lista) - 1) # pega um numero aleatorio 
        try: 
            lista.index(num) # procura o numero e retorna o indice dele
        except ValueError:
            pass

def testar_memoria_lista():
    lista = []
    memory_usage_insercao = memory_profiler.memory_usage((insercoes_lista, (), {'lista':lista,'qnt':consts.QNT_INS}), max_usage=True) # retorna o uso de memoria maxima
    memory_usage_busca = memory_profiler.memory_usage((busca_lista, (), {'lista':lista,   'qnt':consts.QNT_BUSCA}), max_usage=True) # retorna o uso de memoria maxima
    memory_usage_remocao = memory_profiler.memory_usage((remocoes_lista, (), {'lista':lista, 'qnt':consts.QNT_REM}), max_usage=True) # retorna o uso de memoria maxima

    salvar_dados_memoria_csv("listas", memory_usage_insercao, memory_usage_busca, memory_usage_remocao)

def testar_tempo_lista():
    lista = []
    start_time : datetime
    tempo_exec_insert : datetime
    tempo_exec_busca : datetime
    tempo_exec_remocao : datetime

    start_time = datetime.now()
    insercoes_lista(lista, consts.QNT_INS)
    tempo_exec_insert = datetime.now() - start_time

    start_time = datetime.now()
    busca_lista(lista, consts.QNT_BUSCA)
    tempo_exec_busca = datetime.now() - start_time

    start_time = datetime.now()
    remocoes_lista(lista, consts.QNT_REM)
    tempo_exec_remocao = datetime.now() - start_time

    salvar_dados_tempo_csv("listas", tempo_exec_insert, tempo_exec_busca, tempo_exec_remocao)

csv_handler = CSVHandler('data/listas_energia.csv')

def testar_energia_lista():
    lista = []
    with EnergyContext(handler=csv_handler, start_tag='lista') as ctx:
        ctx.record(tag='lista-insercao')
        insercoes_lista(lista, consts.QNT_INS)
        ctx.record(tag='lista-busca')
        busca_lista(lista, consts.QNT_BUSCA)
        ctx.record(tag='lista-remocao')
        remocoes_lista(lista, consts.QNT_REM)

    csv_handler.save_data()
