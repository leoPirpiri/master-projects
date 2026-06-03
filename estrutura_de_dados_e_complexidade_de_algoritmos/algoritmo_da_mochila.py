# ==== Imports ====
import os
from time import time

def mostrar_msg_tempo(msg: str, tempo: float):
	print(f"_____ {msg}: {tempo:.3f} segundos")

# ========= Leitura dos arquivos com a capacidade e itens da mochila ==========

diretorio = './instancias-num/' # Diretório atual
entradas_txt = [f for f in os.listdir(diretorio) if f.startswith('mochila') and f.endswith('.txt')]
for entrada in entradas_txt:
    entrada_mochila = open(f'{diretorio}{entrada}', 'r').readlines()
    print(f"\ninstância: {entrada}")
    # n = número de itens, m = capacidade da mochila
    n, m = map(int, entrada_mochila[0].split())

    # Como o tamanho da mochila já é conhecido, inciamos o array de pesos e valores já com o tamanho necessário (indexado de 1 a n)
    # para evitar o uso de append e futoras alocações dinâmicas, o que pode ser custoso em termos de tempo.
    pesos = [0] * (n + 1)
    valores = [0] * (n + 1)
    
    # Lê os pesos e valores de cada item (indexado de 1 a n)
    for i in range(1, n + 1):
        pesos[i], valores[i] = map(int, entrada_mochila[i].split())
    
    # Matriz de PD inicializada com zeros
    # dp[i][w] guardará o maior valor usando os primeiros 'i' itens com capacidade 'w'
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Construção da tabela de Programação Dinâmica
    inicio_etapa = time()
    for i in range(1, n + 1):
        for w in range(1, m + 1):
            if pesos[i] <= w:
                # Escolha entre incluir ou não o item i
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - pesos[i]] + valores[i])
            else:
                # O item atual é muito pesado para a capacidade w
                dp[i][w] = dp[i-1][w]
    
    valor_maximo = dp[n][m]
    fim_etapa = time()
    
    # Recuperação dos produtos escolhidos (rastreamento reverso)
    produtos_escolhidos = []
    w = m
    for i in range(n, 0, -1):
        # Se o valor mudou em relação à linha anterior, o item foi incluído
        if dp[i][w] != dp[i-1][w]:
            produtos_escolhidos.append(i)
            w -= pesos[i]
            
    # Inverte a lista para mostrar na ordem crescente dos índices
    produtos_escolhidos.reverse()
    
    # Exibe o resultado no formato desejado
    print(f"capacidade da mochila: {m}")
    print(f"valor: {valor_maximo}")
    print(f"produtos escolhidos: {', '.join(map(str, produtos_escolhidos))}")
    mostrar_msg_tempo("Tempo de construção da tabela da mochila", fim_etapa - inicio_etapa)
