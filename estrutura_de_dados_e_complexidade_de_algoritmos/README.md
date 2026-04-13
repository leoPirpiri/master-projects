# Análise de tempo em Algoritmos de Ordenação

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Primeira etapa da atividade de comparação entre o tempo de execução de algoritmos de ordenação. Algoritmos analisados: **Selection Sort**, **Insertion Sort** e **Bubble Sort**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Os arrays de entrada possuem várias contidades de elementos a serem ordenados, sendo eles categorizados da seguinte forma: pequeno, médio e grande.

## Análise gráfica

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Após execução controlada em ambiente com características similares, obtivemos os seguintes resultados para estes 3 algoritmos de ordenação.

### Gráficos de disperção

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Observamos que, como se era de esperar, todos os algoritmos crescem muito rápido (O(n²)). Para vetores de entrada com tamanho relativamente pequenos, quase não se nota a diferença no tempo de execução dos algoritmos, porém, a diferença explode conforme o tamanho aumenta. Além disso, evidenciando a ineficiência do __bubble sort__ com relação aos outros dois algoritmos.

![Gráfico de disperção do tempo da execução dos 3 primeiros algoritmos estudados](assets/grafico_dispersao_completo_3S.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quando aproximamos o gráfico, já descartando os resultados de arrays com tamanho não muito grande, podemos ver que há uma diferença, porém, insignificante, logo o uso de qualquer algoritmo de ordenação não causaria impacto na ordenação de vetores pequenos.

| __Zoom in__ para entradas não muito grandes | __Zoom in__ para entradas onde o 'n' é muito pequeno |
| :---: | :---: |
| ![Gráfico de disperção do tempo da execução com entradas de tamanho não muito grande dos 3 primeiros algoritmos estudados](assets/grafico_dispersao_medio_3S.png) | ![Gráfico de disperção do tempo da execução com entradas muito pequenas dos 3 primeiros algoritmos estudados](assets/grafico_dispersao_pequeno_3S.png) |

### Matrizes de diferença

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Outra forma visual de enxergar o comportamento desses três algoritmos é através de matriz de diferença. Onde, par a par, diferenciamos o tempo médio das ordenações dos vetores com diferentes tamanhos de entrada.

![Matriz de diferença para tempo médio da execução para entradas pequenas dos 3 primeiros algoritmos estudados](assets/matriz_de_diferenca_pequena_3S.png)

| Arrays de entrada média | Array de entrada grande |
| :---: | :---: |
| ![Matriz de diferença para tempo médio da execução para entradas medias dos 3 primeiros algoritmos estudados](assets/matriz_de_diferenca_media_3S.png) | ![Matriz de diferença para tempo médio da execução para entradas grandes dos 3 primeiros algoritmos estudados](assets/matriz_de_diferenca_grande_3S.png) |
