from graficos import fazer_graficos_csv
import lista_tests
import hashtable_tests
import lista_ligada_tests
import shutil
import os

RODAR_LISTAS = True
RODAR_HASHTABLES = True
RODAR_LISTAS_LIGADAS = True

def testar_estrutura_dados():
    # limpar os arquivos csv, e a pasta data
    try:
        os.makedirs("./data", exist_ok=False)
    except FileExistsError:
        shutil.rmtree("./data")
        os.makedirs("./data", exist_ok=True)

    print("Atenção esse programa pode demorar um pouco para rodar, uns 10 minutos")
    if RODAR_LISTAS:
        print("Rodando listas")
        print("Testando Memoria listas")
        lista_tests.testar_memoria_lista()
        print("Testando tempo de execução listas")
        lista_tests.testar_tempo_lista()
        print("Testando energia listas")
        lista_tests.testar_energia_lista()

    if RODAR_HASHTABLES:
        print("Rodando HashTables")
        print("Testando Memoria hashtables")
        hashtable_tests.testar_memoria_hashtable()
        print("Testando tempo de execução hashtables")
        hashtable_tests.testar_tempo_hashtable()
        print("Testando energia hashtables")
        hashtable_tests.testar_energia_hashtable()

    if RODAR_LISTAS_LIGADAS:
        print("Rodando listas_ligadas")
        print("Testando Memoria listas_ligadas")
        lista_ligada_tests.testar_memoria_lista_ligada()
        print("Testando tempo de execução listas_ligadas")
        lista_ligada_tests.testar_tempo_lista_ligada()
        print("Testando energia listas_ligadas")
        lista_ligada_tests.testar_energia_lista_ligada()

def main():
    testar_estruturas = False
    fazer_graficos = False
    
    resp_teste = input("Gostaria de testar as estruturas de dados [s/n] :")
    if resp_teste == "s":
        testar_estruturas = True
    else:
        testar_estruturas = False

    resp_teste = input("Gostaria de fazer os graficos das estruturas de dados [s/n] :")
    if resp_teste == "s":
        fazer_graficos = True
    else:
        fazer_graficos = False

    if testar_estruturas:
        testar_estrutura_dados()
    
    if fazer_graficos:
        fazer_graficos_csv("listas")
        fazer_graficos_csv("hashtables")
        fazer_graficos_csv("lista_ligada")



if __name__ == "__main__":
    main()
