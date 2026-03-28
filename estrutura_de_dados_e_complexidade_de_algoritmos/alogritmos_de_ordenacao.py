import time
import numpy as np
import os
import matplotlib.pyplot as plt

def mostrar_msg_tempo(msg: str, tempo: float):
	print(f"_____ {msg}: {tempo:.3f} segundos")

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        pivo = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > pivo:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pivo

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        indice_menor = i
        for j in range(i+1, n):
            if arr[j] < arr[indice_menor]:
                indice_menor = j
        if arr[i] != arr[indice_menor]:
            aux = arr[i]
            arr[i] = arr[indice_menor]
            arr[indice_menor] = aux

def ler_numeros_por_linha(caminho):
    return np.loadtxt(caminho, dtype=int)

def ordenar_e_cronometrar(arr: list, sort_function: callable):
    inicio_etapa = time.time()
    sort_function(arr)
    fim_etapa = time.time()
    mostrar_msg_tempo("Tempo de ordenação " + sort_function.__name__, fim_etapa - inicio_etapa)
    # print("Array após a ordenação:", arr)
    return [len(arr), fim_etapa - inicio_etapa]

def plotar_resultados(resultados):
    if not resultados:
        print("Nenhum resultado para plotar.")
        return
    selection_q = [r[1] for r in resultados if r[0] == 'selection_sort']
    selection_t = [r[2] for r in resultados if r[0] == 'selection_sort']
    insertion_q = [r[1] for r in resultados if r[0] == 'insertion_sort']
    insertion_t = [r[2] for r in resultados if r[0] == 'insertion_sort']

    plt.figure()
    if selection_q:
        plt.scatter(selection_q, selection_t, color='blue', label='selection_sort')
    if insertion_q:
        plt.scatter(insertion_q, insertion_t, color='red', label='insertion_sort')

    plt.xlabel('Quantidade')
    plt.ylabel('Tempo (segundos)')
    plt.title('Comparação de tempo por algoritmo de ordenação')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Marca o início de toda a tarefa a ser cronometrada.
inicio_tarefa = time.time()
algoritmos_de_ordenacao = {selection_sort.__name__: 'red',
                           insertion_sort.__name__: 'green'}
resultados = {}

# Leitura dos arquivos de entrada.
diretorio = './instancias-num/' # Diretório atual
entradas_in = [f for f in os.listdir(diretorio) if f.endswith('.in')]
for entrada in entradas_in:
    inicio_leitura = time.time()
    entrada_array = ler_numeros_por_linha(f'{diretorio}{entrada}')
    #print("Array antes da ordenação:", entrada_array)
    mostrar_msg_tempo("Tempo de leitura de dados", time.time() - inicio_leitura)

    for algoritmo in algoritmos_de_ordenacao.keys():
        if algoritmo not in resultados.keys():
            resultados[algoritmo] = []
        resultados[algoritmo].append(ordenar_e_cronometrar(entrada_array.copy(), eval(algoritmo)))

print("Resultados após a ordenação:", resultados)
# plotar_resultados(resultados)
# Marca o fim da tarefa e mostra o tempo.
fim_etapa = time.time()
mostrar_msg_tempo("Tempo de execução total", fim_etapa-inicio_tarefa)