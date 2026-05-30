import numpy as np
import pandas as pd
import os
import sys

def prim(n, arestas):
    # Inicializar a matriz de adjacência com zeros
    adj_matrix = [[0] * n for _ in range(n)]
    
    # Preencher a matriz a partir do triângulo superior fornecido
    current_idx = 1
    for u, v, peso in arestas:
        adj_matrix[u][v] = peso
        adj_matrix[v][u] = peso  # O grafo não é direcionado

    # --- Algoritmo de Prim (Abordagem Gulosa) ---
    
    # Configurações iniciais
    key = [float('inf')] * n      # Menores pesos para conectar à MST
    parent = [-1] * n             # Array para armazenar a árvore resultante
    in_mst = [False] * n          # Rastreia os vértices já incluídos na MST
    
    # Começamos pelo vértice 0
    key[0] = 0
    
    for _ in range(n):
        # Passo Guloso: Escolher o vértice com o menor peso (key) 
        # que ainda não está na MST
        min_weight = float('inf')
        u = -1
        for v in range(n):
            if not in_mst[v] and key[v] < min_weight:
                min_weight = key[v]
                u = v
                
        # Inclui o vértice escolhido na MST
        in_mst[u] = True
        
        # Atualiza os pesos dos vértices adjacentes ao vértice escolhido
        for v in range(n):
            # Se v não está na MST, existe a aresta u-v, e o peso dela 
            # é menor do que o peso atual registrado para v
            if adj_matrix[u][v] > 0 and not in_mst[v] and adj_matrix[u][v] < key[v]:
                key[v] = adj_matrix[u][v]
                parent[v] = u

    # --- Exibição do Resultado ---
    # print("\nArestas na Árvore de Espalhamento Mínimo (MST):")
    
    total_weight = 0
    for i in range(1, n):
        # print(f"{parent[i] + 1} <-> {i + 1}    : {adj_matrix[i][parent[i]]}")
        total_weight += adj_matrix[i][parent[i]]
        
    print(f"Custo total utilizando Prim = {total_weight}")

class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])  # Compressão de caminho
        return self.pai[x]

    def union(self, x, y):
        raiz_x = self.find(x)
        raiz_y = self.find(y)

        if raiz_x == raiz_y:
            return False

        # União por rank
        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        elif self.rank[raiz_x] > self.rank[raiz_y]:
            self.pai[raiz_y] = raiz_x
        else:
            self.pai[raiz_y] = raiz_x
            self.rank[raiz_x] += 1

        return True


def kruskal(n, arestas):
    # Ordena as arestas pelo peso
    arestas.sort(key=lambda x: x[2])

    uf = UnionFind(n)

    mst = []
    custo_total = 0

    for u, v, peso in arestas:
        if uf.union(u, v):
            mst.append((u + 1, v + 1, peso))
            custo_total += peso

    return mst, custo_total

# ========= Leitura do triangulo superior da matriz de adjacência ==========
diretorio = './instancias-num/' # Diretório atual
entradas_txt = [f for f in os.listdir(diretorio) if f.endswith('.txt')]
for entrada in entradas_txt:
    entrada_grafo = open(f'{diretorio}{entrada}', 'r').readlines()
    print(f"\nProcessando o grafo do arquivo: {entrada}")
    
    n = int(entrada_grafo[0])

    arestas = []

    for i in range(n - 1):
        valores = list(map(int, entrada_grafo[i + 1].split()))

        for j, peso in enumerate(valores):
            u = i
            v = i + j + 1

            arestas.append((u, v, peso))

    # ========================== Execução algoritmo de Kruskal ==========================

    mst, custo = kruskal(n, arestas)
    # print(f"\nArestas da Árvore Geradora Mínima:")
    # for u, v, peso in mst:
    #     print(f"{u} <-> {v} = {peso}")
    print(f"Custo total utilizando Kruskal = {custo}")

    # ========================== Execução algoritmo de Prim ==========================
    
    prim(n, arestas)
