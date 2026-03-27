import random
import memory_profiler
import consts
from datetime import datetime
from pyJoules.energy_meter import EnergyContext
from pyJoules.handler.csv_handler import CSVHandler
from dados_csv import salvar_dados_memoria_csv, salvar_dados_tempo_csv

def insercoes_hashtable(hashtable: dict, qnt: int):
    for i in range(qnt):
        hashtable[i] = i

def remocoes_hashtable(hashtable: dict, qnt: int):
    for i in range(qnt):
        if i in hashtable:
            del hashtable[i]

def busca_hashtable(hashtable: dict, qnt: int):
    for i in range(qnt):
        num = random.randint(1, consts.QNT_INS - 1)
        _ = hashtable.get(num)

def testar_memoria_hashtable():
    hashtable = {}
    memory_usage_insercao = memory_profiler.memory_usage((insercoes_hashtable, (), {'hashtable': hashtable, 'qnt': consts.QNT_INS}), max_usage=True)
    memory_usage_busca = memory_profiler.memory_usage((busca_hashtable, (), {'hashtable': hashtable, 'qnt': consts.QNT_BUSCA}), max_usage=True)
    memory_usage_remocao = memory_profiler.memory_usage((remocoes_hashtable, (), {'hashtable': hashtable, 'qnt': consts.QNT_REM}), max_usage=True)

    salvar_dados_memoria_csv("hashtables", memory_usage_insercao, memory_usage_busca, memory_usage_remocao)

def testar_tempo_hashtable():
    hashtable = {}
    start_time: datetime
    tempo_exec_insert: datetime
    tempo_exec_busca: datetime
    tempo_exec_remocao: datetime

    start_time = datetime.now()
    insercoes_hashtable(hashtable, consts.QNT_INS)
    tempo_exec_insert = datetime.now() - start_time

    start_time = datetime.now()
    busca_hashtable(hashtable, consts.QNT_BUSCA)
    tempo_exec_busca = datetime.now() - start_time

    start_time = datetime.now()
    remocoes_hashtable(hashtable, consts.QNT_REM)
    tempo_exec_remocao = datetime.now() - start_time

    salvar_dados_tempo_csv("hashtables", tempo_exec_insert, tempo_exec_busca, tempo_exec_remocao)

csv_handler = CSVHandler('data/hashtables_energia.csv')

def testar_energia_hashtable():
    hashtable = {}
    with EnergyContext(handler=csv_handler, start_tag='hashtable') as ctx:
        ctx.record(tag='hashtable-insercao')
        insercoes_hashtable(hashtable, consts.QNT_INS)
        ctx.record(tag='hashtable-busca')
        busca_hashtable(hashtable, consts.QNT_BUSCA)
        ctx.record(tag='hashtable-remocao')
        remocoes_hashtable(hashtable, consts.QNT_REM)
    csv_handler.save_data()
