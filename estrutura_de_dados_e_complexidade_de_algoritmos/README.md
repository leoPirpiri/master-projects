# Análise de tempo em Algoritmos de Ordenação

* [Primeira atividade](#algoritmos-de-ordem-quadrática-on) (Selection Sort, Insertion Sort e Bubble Sort)

* [Segunda atividade](#algoritmos-de-ordem-logarítmica-on-log-n) (Merge Sort e Quick Sort[^1])
[^1]: A complexidade média do Quick Sort é O(n log n), mas pode atingir O(n²) no pior caso.

## Algoritmos de ordem quadrática O(n²)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Primeira etapa da atividade de comparação entre o tempo de execução de algoritmos de ordenação. Algoritmos analisados: **Selection Sort**, **Insertion Sort** e **Bubble Sort**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Os arrays de entrada possuem várias contidades de elementos a serem ordenados, sendo eles categorizados da seguinte forma: pequeno, médio e grande.

### Análise gráfica

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Após execução controlada em ambiente com características similares, obtivemos os seguintes resultados para estes 3 algoritmos de ordenação.

#### Gráficos de disperção

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Observamos que, como se era de esperar, todos os algoritmos crescem muito rápido (O(n²)). Para vetores de entrada com tamanho relativamente pequenos, quase não se nota a diferença no tempo de execução dos algoritmos, porém, a diferença explode conforme o tamanho aumenta. Além disso, evidenciando a ineficiência do __bubble sort__ com relação aos outros dois algoritmos.

![Gráfico de disperção do tempo da execução dos 3 primeiros algoritmos estudados](assets/grafico_dispersao_completo_3S.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quando aproximamos o gráfico, já descartando os resultados de arrays com tamanho não muito grande, podemos ver que há uma diferença, porém, insignificante, logo o uso de qualquer algoritmo de ordenação não causaria impacto na ordenação de vetores pequenos.

| __Zoom in__ para entradas não muito grandes | __Zoom in__ para entradas onde o 'n' é muito pequeno |
| :---: | :---: |
| ![Gráfico de disperção do tempo da execução com entradas de tamanho não muito grande dos 3 primeiros algoritmos estudados](assets/grafico_dispersao_medio_3S.png) | ![Gráfico de disperção do tempo da execução com entradas muito pequenas dos 3 primeiros algoritmos estudados](assets/grafico_dispersao_pequeno_3S.png) |

#### Matrizes de diferença

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Outra forma visual de enxergar o comportamento desses três algoritmos é através de matriz de diferença. Onde, par a par, diferenciamos o tempo médio das ordenações dos vetores com diferentes tamanhos de entrada.

![Matriz de diferença para tempo médio da execução para entradas pequenas dos 3 primeiros algoritmos estudados](assets/matriz_de_diferenca_pequena_3S.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Por exemplo, vemos aqui que a diferença entre o tempo médio de execução do __Insertion sort__ com o __Bubble sort__ é muito forte e evidente, já comparando com __Selection sort__ essa diferença quase não se nota.

| Arrays de entrada média | Arrays de entrada grande |
| :---: | :---: |
| ![Matriz de diferença para tempo médio da execução para entradas medias dos 3 primeiros algoritmos estudados](assets/matriz_de_diferenca_media_3S.png) | ![Matriz de diferença para tempo médio da execução para entradas grandes dos 3 primeiros algoritmos estudados](assets/matriz_de_diferenca_grande_3S.png) |

## Algoritmos de ordem logarítmica O(n log n)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Nesta segunda etapa da atividade de comparação entre o tempo de execução de algoritmos de ordenação. Algoritmos analisados: **Merge Sort** e **Quick Sort**[^1].

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Os arrays de entrada possuem a mesma instância da atividade anterior, sendo eles categorizados da seguinte forma: pequeno, médio e grande.

### Análise gráfica

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Após execução controlada em ambiente com características similares, obtivemos os seguintes resultados para estes outros 2 algoritmos de ordenação.

#### Gráficos de disperção

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Vemos que, os dois novos algoritmos não crescem tão rápido, pois, sua complexidade (O(n log n)) impede a explosão de tempo para entradas grandes. Para vetores de entrada com tamanho relativamente pequenos, quase não se nota a diferença no tempo de execução entre todos os algoritmos (os próximos graficos dá uma visão melhor para instâncias pequenas). Além disso, não evidenciamos vantagem em tempo de execução significante entre o __merge sort__ e quick sort__. A escolha de seu uso parte da análise de suas vantagem e desvantagens em relação a outros aspéquitos como: manutenção na ordem dos elementos, uso de memória extra, etc.

![Gráfico de disperção do tempo da execução dos 5 algoritmos estudados](assets/grafico_dispersao_completo_5S.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quando aproximamos o gráfico, em casos de entrada média, ainda não vemos notória diferença entre o __merge sort__ e quick sort__, inclusive os pontos estão sobrepostos. Já com relação aos algoritmos da primeira etapa, embora ainda mostre melhor eficiência, os tempos são muito parecidos, não havendo real vantagem. Na prática, podemos dizer que algoritmos de ordem quadrática são de uso bem específicos ou apenas didático, por terem facilidade de compreensão, já o __merge sort__ e quick sort__ são mais voltados para ambientes de produção, já que esperamos alto desempenho e eficiência, embora sejam mais complexos de se entender.

| __Zoom in__ para entradas não muito grandes | __Zoom in__ para entradas onde o 'n' é muito pequeno |
| :---: | :---: |
| ![Gráfico de disperção do tempo da execução com entradas de tamanho não muito grande dos 5 primeiros algoritmos estudados](assets/grafico_dispersao_medio_5S.png) | ![Gráfico de disperção do tempo da execução com entradas muito pequenas dos 3 primeiros algoritmos estudados](assets/grafico_dispersao_pequeno_5S.png) |

#### Matrizes de diferença

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quando analisamos a matriz de diferência, essa diferênça não é notória para entrada pequena, o tempo pode se tornar irrelevante para alguns senários.

![Matriz de diferença para tempo médio da execução para entradas pequenas dos 5 primeiros algoritmos estudados](assets/matriz_de_diferenca_pequena_5S.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Embora notamos uma grande discrepância no tempo para grandes entradas, fazendo confirmar o alto desempenho e eficiência entre algoritmos de ordem logarítmica e quadrática. 

| Arrays de entrada média | Arrays de entrada grande |
| :---: | :---: |
| ![Matriz de diferença para tempo médio da execução para entradas medias dos 5 primeiros algoritmos estudados](assets/matriz_de_diferenca_media_5S.png) | ![Matriz de diferença para tempo médio da execução para entradas grandes dos 5 primeiros algoritmos estudados](assets/matriz_de_diferenca_grande_5S.png) |
