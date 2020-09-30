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

- Resultados:
    - 3 arquivos csv com a execução dos k-means para cada caso
    - Resultado do cálculo da pureza e destaque da maior pureza é imprimido na tela