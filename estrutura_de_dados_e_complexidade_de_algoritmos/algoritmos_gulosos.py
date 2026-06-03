import os
import heapq

def prim(n, adj_matrix):
    # --- Algoritmo de Prim (Abordagem Gulosa) ---
    
    # Configurações iniciais
    key = [float('inf')] * n      # Menores pesos para conectar à MST
    parent = [-1] * n             # Array para armazenar a árvore resultante
    in_mst = [False] * n          # Rastreia os vértices já incluídos na MST
    
    # Começamos pelo vértice 0 (o vértice de partida pode ser escolhido aleatoriamente)
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
    return parent

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

def dijkstra(grafo, origem):
    n = len(grafo)

    dist = [float('inf')] * n
    dist[origem] = 0

    visitado = [False] * n

    fila = [(0, origem)]  # (distância, vértice)

    while fila:
        distancia_atual, u = heapq.heappop(fila)

        if visitado[u]:
            continue

        visitado[u] = True

        for v in range(n):
            peso = grafo[u][v]

            if peso > 0 and not visitado[v]:
                nova_dist = distancia_atual + peso

                if nova_dist < dist[v]:
                    dist[v] = nova_dist
                    heapq.heappush(fila, (nova_dist, v))

    return dist

# ========= Leitura do triangulo superior da matriz de adjacência ==========


diretorio = './instancias-num/' # Diretório atual
entradas_txt = [f for f in os.listdir(diretorio) if f.startswith('.dij') and f.endswith('.txt')]
for entrada in entradas_txt:
    entrada_grafo = open(f'{diretorio}{entrada}', 'r').readlines()
    print(f"\nProcessando o grafo do arquivo: {entrada}")
    
    n = int(entrada_grafo[0])
    
    # Inicializar a matriz de adjacência com zeros
    adj_matrix = [[0] * n for _ in range(n)]

    arestas = []

    for i in range(n - 1):
        valores = list(map(int, entrada_grafo[i + 1].split()))

        for j, peso in enumerate(valores):
            u = i
            v = i + j + 1
            # matriz de adjacência
            adj_matrix[u][v] = peso
            adj_matrix[v][u] = peso  # O grafo não é direcionado
            # lista de arestas para Kruskal
            arestas.append((u, v, peso))

    # ========================== Execução algoritmo de Kruskal ==========================

    mst, custo = kruskal(n, arestas)
    # print(f"\nArestas da Árvore Geradora Mínima:")
    # for u, v, peso in mst:
    #     print(f"{u} <-> {v} = {peso}")
    print(f"Custo total utilizando Kruskal = {custo}")

    # ========================== Execução algoritmo de Prim ==========================
    
    parent = prim(n, adj_matrix)
    
    # --- Exibição do Resultado ---
    # print("\nArestas na Árvore de Espalhamento Mínimo (MST):")
    
    total_weight = 0
    for i in range(1, n):
        # print(f"{parent[i] + 1} <-> {i + 1}    : {adj_matrix[i][parent[i]]}")
        total_weight += adj_matrix[i][parent[i]]
        
    print(f"Custo total utilizando Prim = {total_weight}")

    # ========================== Execução algoritmo de Dijkstra ==========================

    # Exemplo: origem = vértice 0
    origem = 0

    distancias = dijkstra(adj_matrix, origem)

    # print("Distâncias mínimas a partir do vértice", origem)
    # for v in range(n):
    #     print(f"{origem} -> {v}: {distancias[v]}")
    
    print(f"Distância mínima da origem escolhida '{origem}' ao último vértice = {distancias[n - 1]}")
    
