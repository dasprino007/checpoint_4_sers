import lista_tests
import hashtable_tests
import lista_ligada_tests

def main():
    print("Atenção esse programa pode demorar um pouco para rodar, uns 10 minutos")
    print("Rodando listas")
    lista_tests.testar_memoria_lista()
    lista_tests.testar_tempo_lista()
    lista_tests.testar_energia_lista()

    print("Rodando HashTables")
    hashtable_tests.testar_memoria_hashtable()
    hashtable_tests.testar_tempo_hashtable()
    hashtable_tests.testar_energia_hashtable()

    print("Rodando listas_ligadas")
    lista_ligada_tests.testar_memoria_lista_ligada()
    lista_ligada_tests.testar_tempo_lista_ligada()
    lista_ligada_tests.testar_energia_lista_ligada()


if __name__ == "__main__":
    main()
