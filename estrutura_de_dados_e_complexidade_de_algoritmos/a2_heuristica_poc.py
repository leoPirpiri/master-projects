import os
import time

def ler_instancia(instancia):
    entrada_mochila = open(f'{diretorio}{instancia}', 'r').readlines()
    # print(f"\ninstância: {instancia}")
    # n = número de itens, m = capacidade da mochila
    n, capacidade = map(int, entrada_mochila[0].split())

    solucao = entrada_mochila[n+1].split()
    # Como o tamanho da mochila já é conhecido, inciamos o array de pesos e valores já com o tamanho necessário (indexado de 1 a n)
    # para evitar o uso de append e futoras alocações dinâmicas, o que pode ser custoso em termos de tempo.
    pesos = [0] * (n)
    valores = [0] * (n)
    valor_otimo = 0;
    peso_otimo = 0;
    
    # Lê os pesos e valores de cada item (indexado de 1 a n)
    for i in range(0, n):
        valores[i], pesos[i] = map(int, entrada_mochila[i+1].split())
        if solucao[i] == '1':
            peso_otimo += pesos[i]
            valor_otimo += valores[i]


    return pesos, valores, capacidade, valor_otimo, peso_otimo

def heuristica_construcao(pesos, valores, capacidade):
    n = len(pesos)
    # Calcula a eficiência (valor/peso) e guarda o índice original do item
    eficiencia = [(valores[i] / pesos[i], i) for i in range(n)]
    # Ordena de forma decrescente pela eficiência
    eficiencia.sort(key=lambda x: x[0], reverse=True)
    
    solucao = [0] * n
    peso_atual = 0
    valor_atual = 0
    
    for _, i in eficiencia:
        if peso_atual + pesos[i] <= capacidade:
            solucao[i] = 1
            peso_atual += pesos[i]
            valor_atual += valores[i]
            
    return solucao, valor_atual, peso_atual

def vizinhanca_inserir_remover(solucao, pesos, valores, capacidade, valor_atual, peso_atual):
    """ Vizinhança 1: Inverte o estado de 1 bit (0->1 ou 1->0) """
    melhor_solucao = list(solucao)
    melhor_valor = valor_atual
    melhor_peso = peso_atual
    melhorou = False
    
    for i in range(len(solucao)):
        nova_solucao = list(solucao)
        
        if solucao[i] == 0: # Tenta colocar o item
            novo_peso = peso_atual + pesos[i]
            if novo_peso <= capacidade:
                novo_valor = valor_atual + valores[i]
                if novo_valor > melhor_valor:
                    nova_solucao[i] = 1
                    melhor_solucao = nova_solucao
                    melhor_valor = novo_valor
                    melhor_peso = novo_peso
                    melhorou = True
        else: # Tenta tirar o item
            novo_peso = peso_atual - pesos[i]
            novo_valor = valor_atual - valores[i]
            if novo_valor > melhor_valor: # Raro, mas possível em outras estruturas
                nova_solucao[i] = 0
                melhor_solucao = nova_solucao
                melhor_valor = novo_valor
                melhor_peso = novo_peso
                melhorou = True
                
    return melhor_solucao, melhor_valor, melhor_peso, melhorou


def vizinhanca_troca(solucao, pesos, valores, capacidade, valor_atual, peso_atual):
    """ Vizinhança 2: Troca um item de dentro por um de fora da mochila """
    n = len(solucao)
    melhor_solucao = list(solucao)
    melhor_valor = valor_atual
    melhor_peso = peso_atual
    melhorou = False
    
    # Identifica índices de itens dentro e fora
    dentro = [i for i in range(n) if solucao[i] == 1]
    fora = [j for j in range(n) if solucao[j] == 0]
    
    for i in dentro:
        for j in fora:
            # Peso ao tirar i e colocar j
            novo_peso = peso_atual - pesos[i] + pesos[j]
            if novo_peso <= capacidade:
                novo_valor = valor_atual - valores[i] + valores[j]
                if novo_valor > melhor_valor:
                    nova_solucao = list(solucao)
                    nova_solucao[i] = 0
                    nova_solucao[j] = 1
                    melhor_solucao = nova_solucao
                    melhor_valor = novo_valor
                    melhor_peso = novo_peso
                    melhorou = True
                    
    return melhor_solucao, melhor_valor, melhor_peso, melhorou

def executar_vnd(sol_inicial, v_inicial, p_inicial, pesos, valores, capacidade):
    sol_atual = list(sol_inicial)
    v_atual = v_inicial
    p_atual = p_inicial
    
    k = 1
    k_max = 2
    
    while k <= k_max:
        if k == 1:
            nova_sol, novo_v, novo_p, melhorou = vizinhanca_inserir_remover(
                sol_atual, pesos, valores, capacidade, v_atual, p_atual
            )
        elif k == 2:
            nova_sol, novo_v, novo_p, melhorou = vizinhanca_troca(
                sol_atual, pesos, valores, capacidade, v_atual, p_atual
            )
            
        if melhorou:
            sol_atual = nova_sol
            v_atual = novo_v
            p_atual = novo_p
            k = 1 # Retorna para a primeira vizinhança ao encontrar melhora
        else:
            k += 1 # Vai para a próxima vizinhança se falhar em melhorar
            
    return sol_atual, v_atual, p_atual

######################################## == ########################################
#  EXECUÇÃO

# Lista de arquivos de entrada (instâncias) para teste.
diretorio = './instancias-num/' # Diretório atual
entradas_txt = [f for f in os.listdir(diretorio) if f.startswith('knapPI_')]
entradas_txt.sort(key=lambda x: int(x.split('_')[2])) # Ordena para garantir a ordem correta das instâncias
num_execucoes = 10 # Para tirar a média do tempo computacional

print(f"{'Nº Itens':<10} | {'Capacidade':<15} | {'Peso Ótimo':<15} | {'Val. Inicial':<15} | {'Melhor VND':<15} | {'Val. Ótimo':<15} | {'Tempo Médio (s)':<15}")
print("-" * 100)

for instancia in entradas_txt:
    pesos, valores, capacidade, valor_otimo, peso_otimo = ler_instancia(instancia)
    
    # 1. Gera solução inicial
    sol_ini, v_ini, p_ini = heuristica_construcao(pesos, valores, capacidade)
    
    # 2. Roda o VND múltiplas vezes para medir o tempo médio com precisão
    tempos = []
    melhor_v_vnd = 0
    
    for _ in range(num_execucoes):
        inicio = time.perf_counter()
        _, v_vnd, _ = executar_vnd(sol_ini, v_ini, p_ini, pesos, valores, capacidade)
        fim = time.perf_counter()
        
        tempos.append(fim - inicio)
        melhor_v_vnd = max(melhor_v_vnd, v_vnd) # Garante o registro do melhor pico
        
    tempo_medio = sum(tempos) / len(tempos)
    
    print(f"{len(valores):<10} | {capacidade:<15} | {peso_otimo:<15} | {v_ini:<15} | {melhor_v_vnd:<15} | {valor_otimo:<15} | {tempo_medio:<15.6f}")
