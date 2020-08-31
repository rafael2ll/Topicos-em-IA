Integrantes:
    - Rafael Valentim Silva:    11711BCC010
    - Luis Benito Sanches:      11621BCC022

- Requisitos:
   - Python3.0 ou superior

- Comandos:
    Para distancia euclidiana:
        - python3 main.py "caminho_do_arquivo_de_entrada" --distance euclidean

    Para distancia Manhattan:
        - python3 main.py "caminho_do_arquivo_de_entrada" --distance manhattan

   Caso o arquivo possua header com nome das colunas:
    - python3 main.py "caminho_do_arquivo_de_entrada" --has-header=true

   Para mais variaçoes, execute o seguinte comando:
    - python3 main.py -h

- Resultados:
    - Um arquivo csv na pasta que o comando foi executado contendo o nome do arquivo de entrada + _dist.csv