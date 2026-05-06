# Abrir um arquivo para escrita 
with open('arquivo.txt','w') as file:
    file.write('Olá, mundo!')

# Abrir um arquivo para leitura e escrita
with open('arquivo.txt', 'r+') as file:
    conteudo = file.read()
    file.write('\nAdicionando mais conteúdo.')

# Abrir um arquivo para anexo
with open('arquivo.txt', 'a') as file:
    file.write('\nMais uma linha no final do arquivo')

# Abre o arquivo no modo de escrita ('w')
with open('arquivo.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')