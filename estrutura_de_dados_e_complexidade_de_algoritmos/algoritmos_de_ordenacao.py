import time
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(3000)

def mostrar_msg_tempo(msg: str, tempo: float):
	print(f"_____ {msg}: {tempo:.3f} segundos")

def ordenar_e_cronometrar(arr: list, sort_function: callable):
    inicio_etapa = time.time()
    sort_function(arr)
    fim_etapa = time.time()
    mostrar_msg_tempo("Tempo de ordenação " + sort_function.__name__, fim_etapa - inicio_etapa)
    # print("Array após a ordenação:", arr)
    return [len(arr), fim_etapa - inicio_etapa]

def ler_numeros_por_linha(caminho):
    return np.loadtxt(caminho, dtype=int)

# Início do grupo de funções de ordenação

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        pivo = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > pivo:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pivo

# Selection Sort
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

def bubble_sort(arr):
    n = len(arr)
    while True:
        trocou = False
        for i in range(n-1):
             if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                trocou = True
        if not trocou:
            break

def merge_sort(arr):
    if len(arr) > 1:
        # 1. Divide: Encontra o meio da lista
        meio = len(arr) // 2
        metade_esquerda = arr[:meio]
        metade_direita = arr[meio:]

        # 2. Recursão: Ordena as duas metades
        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        # 3. Conquista: Mescla as metades de volta
        i = j = k = 0
        
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                arr[k] = metade_esquerda[i]
                i += 1
            else:
                arr[k] = metade_direita[j]
                j += 1
            k += 1

        # Verifica se sobrou algum elemento em qualquer uma das partes
        while i < len(metade_esquerda):
            arr[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            arr[k] = metade_direita[j]
            j += 1
            k += 1

def quick_sort(arr):
    # Caso base: listas com 0 ou 1 elemento já estão ordenadas
    if len(arr) <= 1:
        return arr
    else:
        # Escolhendo o pivô (ex: último elemento)
        pivo = arr[-1]
        
        # Particionamento
        menores = [x for x in arr[:-1] if x <= pivo]
        maiores = [x for x in arr[:-1] if x > pivo]
        
        # Recursão e Concatenação
        return quick_sort(menores) + [pivo] + quick_sort(maiores)

# Final do grupo de funções de ordenação

# Lista de algoritmos de ordenação a serem testados.
# Antes de inserir o algoritmo de ordenação ao dicionário,
# certifique-se de que a função do algoritmo de ordenação esteja anteriormente definida no código.
# A cor associada a cada algoritmo é apenas para fins de visualização no gráfico.
algoritmos_de_ordenacao = {quick_sort.__name__: 'purple',
                           merge_sort.__name__: 'orange',
                           insertion_sort.__name__: 'green',
                           selection_sort.__name__: 'red',
                           bubble_sort.__name__: 'blue'
                           }

def plotar_resultados(resultados):
    if not resultados:
        print("Nenhum resultado para plotar.")
        return
    valores_medios = pd.DataFrame(columns=['nome','quantidade', 'tempo'])
    
    for algoritmo, valores in resultados.items():
        tratamento_valores = pd.DataFrame(valores, columns=['quantidade', 'tempo'])
        tratamento_valores['nome'] = algoritmo
        plt.scatter(tratamento_valores['quantidade'], tratamento_valores['tempo'], color=algoritmos_de_ordenacao[algoritmo], label=algoritmo, s=10)
        valores_medios = pd.concat([valores_medios, tratamento_valores.groupby(['nome', 'quantidade'])['tempo'].mean().reset_index()], ignore_index=True)
    
    plt.xlabel('Tamanho do Array (n)')
    plt.ylabel('Tempo (segundos)')
    plt.title('Comparação de tempo por algoritmo de ordenação')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    print("Valores médios por algoritmo:\n", valores_medios)
    tempos_medios = [
        valores_medios[valores_medios['quantidade'] == 1001],
        valores_medios[valores_medios['quantidade'] == 10001],
        valores_medios[valores_medios['quantidade'] == 100001]]

    if tempos_medios:
        algorithms = tempos_medios[0]['nome'].tolist()
        figuras = []
        for i in range(len(tempos_medios)):
            if not tempos_medios[i].empty:
                fig, ax = plt.subplots()
                # Labels
                ax.set_xticks(range(len(algorithms)))
                ax.set_yticks(range(len(algorithms)))
                ax.set_xticklabels(algorithms)
                ax.set_yticklabels(algorithms)
                ax.xaxis.set_ticks_position('top')
                ax.xaxis.set_label_position('top')
                ax.set_title(f"Matriz de Diferença (n={tempos_medios[i]['quantidade'].iloc[0]})")

                # Rotacionar eixo X
                plt.setp(ax.get_xticklabels(), rotation=45, ha='left')

                tempos = np.array(tempos_medios[i]['tempo'])
                # Matriz de diferença
                diff = tempos.reshape(-1, 1) - tempos
                # Heatmap
                max_abs = np.abs(diff).max()
                im = ax.imshow(diff, cmap='coolwarm', vmin=-max_abs, vmax=max_abs)
                plt.tight_layout()
                figuras.append((ax, diff))

        # Valores dentro das células
        for i in range(len(algorithms)):
            for j in range(len(algorithms)):
                for k in range(len(figuras)):
                    figuras[k][0].text(j, i, f"{figuras[k][1][i, j]:.3f}", ha="center", va="center")
    plt.show()


# Marca o início de toda a tarefa a ser cronometrada.
inicio_tarefa = time.time()
resultados = {}

# Leitura dos arquivos de entrada.
diretorio = './instancias-num/' # Diretório atual
entradas_in = [f for f in os.listdir(diretorio) if f.endswith('.in')]
for entrada in entradas_in:
    inicio_leitura = time.time()
    entrada_array = ler_numeros_por_linha(f'{diretorio}{entrada}')
    print("Array antes da ordenação:", entrada_array)
    mostrar_msg_tempo("Tempo de leitura de dados", time.time() - inicio_leitura)

    for algoritmo in algoritmos_de_ordenacao.keys():
        if algoritmo not in resultados.keys():
            resultados[algoritmo] = []
        resultados[algoritmo].append(ordenar_e_cronometrar(entrada_array.copy(), eval(algoritmo)))

# print("Resultados após a ordenação:\n", resultados)
# Marca o fim da tarefa e mostra o tempo.
fim_etapa = time.time()
plotar_resultados(resultados)

mostrar_msg_tempo("Tempo de execução total", fim_etapa-inicio_tarefa)