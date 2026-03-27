import random
import memory_profiler
import consts
from datetime import datetime
from pyJoules.energy_meter import EnergyContext
from pyJoules.handler.csv_handler import CSVHandler
from dados_csv import salvar_dados_memoria_csv, salvar_dados_tempo_csv


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def index(self, value):
        current = self.head
        idx = 0
        while current:
            if current.value == value:
                return idx
            current = current.next
            idx += 1
        raise ValueError(f'{value} não encontrado na lista ligada')


def insercoes_lista_ligada(lista: LinkedList, qnt: int):
    for i in range(qnt):
        lista.append(i)

def remocoes_lista_ligada(lista: LinkedList, qnt: int):
    for i in range(qnt):
        lista.remove(i)

def busca_lista_ligada(lista: LinkedList, qnt: int):
    for i in range(qnt):
        num = random.randint(1, lista.size - 1)
        try:
            lista.index(num)
        except ValueError:
            pass

def testar_memoria_lista_ligada():
    lista = LinkedList()
    memory_usage_insercao = memory_profiler.memory_usage((insercoes_lista_ligada, (), {'lista': lista, 'qnt': consts.QNT_INS}), max_usage=True)
    memory_usage_busca = memory_profiler.memory_usage((busca_lista_ligada, (), {'lista': lista, 'qnt': consts.QNT_BUSCA}), max_usage=True)
    memory_usage_remocao = memory_profiler.memory_usage((remocoes_lista_ligada, (), {'lista': lista, 'qnt': consts.QNT_REM}), max_usage=True)
    
    salvar_dados_memoria_csv("listas_ligada", memory_usage_insercao, memory_usage_busca, memory_usage_remocao)

def testar_tempo_lista_ligada():
    lista = LinkedList()
    start_time: datetime
    tempo_exec_insert: datetime
    tempo_exec_busca: datetime
    tempo_exec_remocao: datetime

    start_time = datetime.now()
    insercoes_lista_ligada(lista, consts.QNT_INS)
    tempo_exec_insert = datetime.now() - start_time

    start_time = datetime.now()
    busca_lista_ligada(lista, consts.QNT_BUSCA)
    tempo_exec_busca = datetime.now() - start_time

    start_time = datetime.now()
    remocoes_lista_ligada(lista, consts.QNT_REM)
    tempo_exec_remocao = datetime.now() - start_time

    salvar_dados_tempo_csv("lista_ligada", tempo_exec_insert, tempo_exec_busca, tempo_exec_remocao)

csv_handler = CSVHandler('data/lista_ligada_energia.csv')

def testar_energia_lista_ligada():
    lista = LinkedList()
    with EnergyContext(handler=csv_handler, start_tag='lista-ligada') as ctx:
        ctx.record(tag='lista-ligada-insercao')
        insercoes_lista_ligada(lista, consts.QNT_INS)
        ctx.record(tag='lista-ligada-busca')
        busca_lista_ligada(lista, consts.QNT_BUSCA)
        ctx.record(tag='lista-ligada-remocao')
        remocoes_lista_ligada(lista, consts.QNT_REM)
    csv_handler.save_data()
