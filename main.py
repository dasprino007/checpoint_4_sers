import lista_tests
import hashtable_tests
import lista_ligada_tests
import shutil
import os

RODAR_LISTAS = True
RODAR_HASHTABLES = True
RODAR_LISTAS_LIGADAS = True

def main():
    # limpar os arquivos csv, e a pasta data
    try:
        os.makedirs("./data", exist_ok=False)
    except FileExistsError:
        shutil.rmtree("./data")
        os.makedirs("./data", exist_ok=True)

    print("Atenção esse programa pode demorar um pouco para rodar, uns 10 minutos")
    if RODAR_LISTAS:
        print("Rodando listas")
        lista_tests.testar_memoria_lista()
        lista_tests.testar_tempo_lista()
        lista_tests.testar_energia_lista()

    if RODAR_HASHTABLES:
        print("Rodando HashTables")
        hashtable_tests.testar_memoria_hashtable()
        hashtable_tests.testar_tempo_hashtable()
        hashtable_tests.testar_energia_hashtable()

    if RODAR_LISTAS_LIGADAS:
        print("Rodando listas_ligadas")
        lista_ligada_tests.testar_memoria_lista_ligada()
        lista_ligada_tests.testar_tempo_lista_ligada()
        lista_ligada_tests.testar_energia_lista_ligada()


if __name__ == "__main__":
    main()
