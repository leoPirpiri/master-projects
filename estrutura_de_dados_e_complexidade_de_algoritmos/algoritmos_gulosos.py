import numpy as np
import pandas as pd
import os

def prim():
    pass

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
    
    n = int(entrada_grafo[0])

    arestas = []

    for i in range(n - 1):
        valores = list(map(int, entrada_grafo[i + 1].split()))

        for j, peso in enumerate(valores):
            u = i
            v = i + j + 1

            arestas.append((u, v, peso))

    # ========================== Executa Kruskal ==========================

    mst, custo = kruskal(n, arestas)

    print("Arestas da Árvore Geradora Mínima:")
    for u, v, peso in mst:
        print(f"{u} <-> {v} = {peso}")

    print(f"Total = {custo}")
