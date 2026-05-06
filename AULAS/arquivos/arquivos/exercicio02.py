# 1. Pede os nomes dos arquivos, arquiuvo.txt e meuarquivo.txt
arquivo1 = input("Nome do primeiro arquivo: ")
arquivo2 = input("Nome do segundo arquivo: ")
arquivo_final = input("Nome do novo arquivo: ")

# 2. Lê o conteúdo dos dois arquivos, e coloca eles em variáveis
conteudo1 = open(arquivo1, 'r', encoding='UTF-8').read()
conteudo2 = open(arquivo2, 'r', encoding='UTF-8').read()

# 3. Cria o novo arquivo e grava os conteúdos (concatenando), é mais fácil juntar duas variáveis
with open(arquivo_final, 'w', encoding='UTF-8') as destino:
    destino.write(conteudo1)
    destino.write('\n') 
    destino.write(conteudo2)
