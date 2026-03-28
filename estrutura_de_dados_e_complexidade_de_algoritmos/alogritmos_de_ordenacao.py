import time
import numpy as np
import os

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
    return [sort_function.__name__, len(arr), fim_etapa - inicio_etapa]

# Marca o início de toda a tarefa a ser cronometrada.
inicio_tarefa = time.time()
resultados = []

# Leitura dos arquivos de entrada.
diretorio = './instancias-num/' # Diretório atual
entradas_in = [f for f in os.listdir(diretorio) if f.endswith('.in')]
for entrada in entradas_in:
    inicio_leitura = time.time()
    entrada_array = ler_numeros_por_linha(f'{diretorio}{entrada}')
    #print("Array antes da ordenação:", entrada_array)
    mostrar_msg_tempo("Tempo de leitura de dados", time.time() - inicio_leitura)

    # inicio da ordenação usando o Selection Sort
    resultados.append(ordenar_e_cronometrar(entrada_array.copy(), selection_sort))

    # inicio da ordenação usando o Insertion Sort
    resultados.append(ordenar_e_cronometrar(entrada_array.copy(), insertion_sort))

    # inicio da ordenação usando Quick Sort
    # resultados.append(ordenar_e_cronometrar(entrada_array.copy(), quick_sort()))

print("Resultados após a ordenação:", resultados)
# Marca o fim da tarefa e mostra o tempo.
fim_etapa = time.time()
mostrar_msg_tempo("Tempo de execução total", fim_etapa-inicio_tarefa)