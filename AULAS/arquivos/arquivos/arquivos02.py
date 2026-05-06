with open ('arquivo.txt', 'r') as file:
    # Lê todo o conteúdo do arquivo

    conteudo = file.read()
    print(conteudo)

#  Abre o arquivo no modo leitura ('r')

with open('arquivo.txt', 'r') as file:
    # Lê a primeira linha do arquivo:
    linha1 = file.readline()
    # Lê a segunda linha do arquivo:
    linha2 = file.readline()
    # Lê a terceira linha do arquivo:
    linha3 = file.readline()
    print(linha1)
    print(linha2)
    print(linha3)