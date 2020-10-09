Integrantes:
    - Rafael Valentim Silva:    11711BCC010
    - Luis Benito Sanches:      11621BCC022

- Requisitos:
   - Python3.0 ou superior
   - Executar: pip3 install numpy
   
- Comandos:
    - python3 main.py "caminho_do_arquivo_de_entrada"
    - Exemplo: python3 main.py ./data/iris.csv

   Caso o arquivo possua header com nome das colunas:
    - python3 main.py "caminho_do_arquivo_de_entrada" --has-header=true

   Para mais variaçoes, execute o seguinte comando:
    - python3 main.py -h

- Resultados:
    - 3 arquivos csv na pasta que o comando foi executado contendo o resultado da execução dos 3 k-means
    - No console de execução mostra o passo-a-passo do cálculo do SSWC  e a sumarização final.