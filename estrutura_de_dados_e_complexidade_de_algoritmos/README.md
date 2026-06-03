# Unidade 1 - Análise de tempo em algoritmos de ordenação

- [Primeira atividade](#algoritmos-de-ordem-quadrática-on) (Selection Sort, Insertion Sort e Bubble Sort)

- [Segunda atividade](#algoritmos-de-ordem-logarítmica-on-log-n) (Merge Sort e Quick Sort[^1])
  [^1]: A complexidade média do Quick Sort é O(n log n), mas pode atingir O(n²) no pior caso.

## Algoritmos de ordem quadrática O(n²)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Primeira etapa da atividade de comparação entre o tempo de execução de algoritmos de ordenação. Algoritmos analisados: **Selection Sort**, **Insertion Sort** e **Bubble Sort**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Os arrays de entrada possuem várias quantidades de elementos a serem ordenados, sendo eles categorizados da seguinte forma: pequeno, médio e grande.

### Análise gráfica

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Após execução controlada em ambiente com características similares, obtivemos os seguintes resultados para estes 3 algoritmos de ordenação.

#### Gráficos de dispersão

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Observamos que, como era de se esperar, todos os algoritmos crescem muito rápido (O(n²)). Para vetores de entrada com tamanhos relativamente pequenos, quase não se nota a diferença no tempo de execução dos algoritmos; porém, a diferença explode conforme o tamanho aumenta. Além disso, evidenciando a ineficiência do **bubble sort** em relação aos outros dois algoritmos.

![Gráfico de disperção do tempo da execução dos 3 primeiros algoritmos estudados](assets/grafico_dispersao_completo_3S.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quando aproximamos o gráfico, já descartando os resultados de arrays com tamanho não muito grande, podemos ver que há uma diferença, porém insignificante; logo o uso de qualquer algoritmo de ordenação não causaria impacto na ordenação de vetores pequenos.

|                                                            **Zoom in** para entradas não muito grandes                                                            |                                                  **Zoom in** para entradas onde o 'n' é muito pequeno                                                  |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![Gráfico de disperção do tempo da execução com entradas de tamanho não muito grande dos 3 primeiros algoritmos estudados](assets/grafico_dispersao_medio_3S.png) | ![Gráfico de disperção do tempo da execução com entradas muito pequenas dos 3 primeiros algoritmos estudados](assets/grafico_dispersao_pequeno_3S.png) |

#### Matrizes de diferença

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Outra forma visual de enxergar o comportamento desses três algoritmos é por meio de matriz de diferença. Onde, par a par, diferenciamos o tempo médio das ordenações dos vetores com diferentes tamanhos de entrada.

![Matriz de diferença para tempo médio da execução para entradas pequenas dos 3 primeiros algoritmos estudados](assets/matriz_de_diferenca_pequena_3S.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Por exemplo, vemos aqui que a diferença entre o tempo médio de execução do **Insertion Sort** com o **Bubble Sort** é muito forte e evidente, já comparando com **Selection Sort** essa diferença quase não se nota.

|                                                                Arrays de entrada média                                                                 |                                                                 Arrays de entrada grande                                                                 |
| :----------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![Matriz de diferença para tempo médio da execução para entradas medias dos 3 primeiros algoritmos estudados](assets/matriz_de_diferenca_media_3S.png) | ![Matriz de diferença para tempo médio da execução para entradas grandes dos 3 primeiros algoritmos estudados](assets/matriz_de_diferenca_grande_3S.png) |

## Algoritmos de ordem logarítmica O(n log n)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Nesta segunda etapa da atividade de comparação entre o tempo de execução de algoritmos de ordenação. Algoritmos analisados: **Merge Sort** e **Quick Sort**[^1].

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Os arrays de entrada possuem a mesma instância da atividade anterior, sendo eles categorizados da seguinte forma: pequeno, médio e grande.

### Análise gráfica

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Após execução controlada em ambiente com características similares, obtivemos os seguintes resultados para estes outros 2 algoritmos de ordenação.

#### Gráficos de dispersão

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Vemos que os dois novos algoritmos não crescem tão rápido, pois sua complexidade (O(n log n)) impede a explosão de tempo para entradas grandes. Para vetores de entrada com tamanhos relativamente pequenos, quase não se nota a diferença no tempo de execução entre todos os algoritmos (os próximos graficos dão uma visão melhor para instâncias pequenas). Além disso, não evidenciamos vantagem em tempo de execução significativa entre o **Merge Sort** e **Quick Sort**. A escolha de seu uso parte da análise de suas vantagens e desvantagens em relação a outros aspectos como: manutenção na ordem dos elementos, uso de memória extra, etc.

![Gráfico de disperção do tempo da execução dos 5 algoritmos estudados](assets/grafico_dispersao_completo_5S.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quando aproximamos o gráfico, em casos de entrada média, ainda não vemos notória diferença entre o **Merge Sort** e **Quick Sort**, inclusive os pontos estão sobrepostos. Já com relação aos algoritmos da primeira etapa, embora ainda mostre melhor eficiência, os tempos são muito parecidos, não havendo real vantagem. Na prática, podemos dizer que algoritmos de ordem quadrática são de uso bem específicos ou apenas didático, por terem facilidade de compreensão, já o **Merge Sort** e **Quick Sort** são mais voltados para ambientes de produção, já que esperamos alto desempenho e eficiência, embora sejam mais complexos de se entender.

|                                                            **Zoom in** para entradas não muito grandes                                                            |                                                  **Zoom in** para entradas onde o 'n' é muito pequeno                                                  |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![Gráfico de disperção do tempo da execução com entradas de tamanho não muito grande dos 5 primeiros algoritmos estudados](assets/grafico_dispersao_medio_5S.png) | ![Gráfico de disperção do tempo da execução com entradas muito pequenas dos 3 primeiros algoritmos estudados](assets/grafico_dispersao_pequeno_5S.png) |

#### Matrizes de diferença

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quando analisamos a matriz de diferença, essa diferença não é notória para entrada pequena; o tempo pode se tornar irrelevante para alguns cenários.

![Matriz de diferença para tempo médio da execução para entradas pequenas dos 5 primeiros algoritmos estudados](assets/matriz_de_diferenca_pequena_5S.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Embora notemos uma grande discrepância no tempo para grandes entradas, isso confirma o alto desempenho e eficiência entre algoritmos de ordem logarítmica e quadrática.

|                                                                Arrays de entrada média                                                                 |                                                                 Arrays de entrada grande                                                                 |
| :----------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![Matriz de diferença para tempo médio da execução para entradas medias dos 5 primeiros algoritmos estudados](assets/matriz_de_diferenca_media_5S.png) | ![Matriz de diferença para tempo médio da execução para entradas grandes dos 5 primeiros algoritmos estudados](assets/matriz_de_diferenca_grande_5S.png) |

# Unidade 2 - Análise de algoritmos gulosos

- [Primeira atividade](#árvore-de-espalhamento-e-caminho-mínimo) (Kruskal & Prim)

- [Segunda atividade](#problema-da-mochila-inteira) (Problema da mochila)

## Árvore de espalhamento e caminho mínimo

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Algoritmos gulosos (Greedy Algorithms) constroem uma solução passo a passo, escolhendo em cada etapa a opção que parece ser a melhor decisão local naquele momento. O problema que devemos atentar para as várias abordagens usando essa estratégia é a quantidade de vértices, pois, na tentativa de achar a solução ótima, aumentamos muito o custo de processamento e memória.

### Problema da árvore de espalhamento mínimo (**Kruskal**, **Prim**)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; O algoritmo de Kruskal utiliza uma abordagem gulosa para selecionar as arestas de menor peso, garantindo que não haja ciclos durante a construção da árvore. Isso permite encontrar uma solução ótima para o problema da árvore geradora mínima de forma eficiente, sendo bastante utilizado em problemas de redes e otimização.

**Complexidade:** O(E log V)[^2]
[^2]: Onde V e E são, respectivamente, os conjuntos/quantidades de vértices e arestas do grafo.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; O algoritmo de Prim também encontra uma **Árvore Geradora Mínima**, porém utilizando uma abordagem diferente. A árvore é expandida gradualmente a partir de um vértice inicial, sempre escolhendo a aresta de menor custo que conecta um vértice já visitado a um vértice ainda não visitado.

**Complexidade:** O(E log E)[^2]

### Problema do caminho mínimo (**Dijkstra**)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Para o problema do Caminho Mínimo, utilizamos o algoritmo de Dijkstra. Em cada passo, o vértice com menor distância conhecida é selecionado e suas arestas são relaxadas para atualizar possíveis caminhos mais curtos.

**Complexidade:** O(E log V)[^2]

### Comparação

| Algoritmo | Problema Resolvido     | Permite Pesos Negativos |
| --------- | ---------------------- | ----------------------- |
| Kruskal   | Árvore Geradora Mínima | Sim                     |
| Prim      | Árvore Geradora Mínima | Sim                     |
| Dijkstra  | Caminho Mínimo         | Não                     |

## Problema da mochila inteira

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; O problema da Mochila 0-1 consiste em selecionar um subconjunto de itens (peso, valor) para maximizar o valor total transportado sem ultrapassar a capacidade da mochila. Cada item pode ser escolhido apenas uma vez (0 ou 1). É um problema clássico de otimização resolvido por Programação Dinâmica (DP)

- Estrutura de Dados: Uma tabela bidimensional dp de tamanho (n + 1) x (M + 1) armazena as soluções dos subproblemas.
- Complexidade de Tempo: O algoritmo roda em tempo O(n x M).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Após realizar os testes com as entradas simples e confirmar que o algoritmo funcionava, testamos o algoritmo feito com as entradas disponibilizadas na atividade e pode-se notar uma demora ao mostrar os resultado. Usando um meio para cronometrar o tempo na construção da tabela, mostra-se um aumento de tempo considerável nesta construção, isso devido ao aumento da capacidade da mochila.

![Resultados após execução da PD sobre o problema da mochila](assets/tempo_construcao_matriz_pd.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Isso mostra que para instâncias onde a capacidade da mochila assume valores massivos, o custo computacional de tempo e de memória[^3] pode se tornar um gargalo substancial.
[^3]: Os teste de medição da alocação de memória não foram realizados nesta atividade, mas é um bom ponto a se pensar no futuro.
