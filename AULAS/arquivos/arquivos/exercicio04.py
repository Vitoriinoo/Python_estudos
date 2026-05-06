with open('ambos.txt', 'r', encoding='utf-8') as arquivo_origem:
    linhas = arquivo_origem.readlines()

linhas.sort()

with open('saida.txt', 'w', encoding='utf-8') as arquivo_destino:
    arquivo_destino.writelines(linhas)