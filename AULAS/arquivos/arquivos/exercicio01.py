with open ('meuarquivo.txt', 'r', encoding='UTF-8') as file:
    # Lê todo o conteúdo do arquivo

    conteudo = file.read()
    palavras = conteudo.split()
    quantidade = len(palavras)
    print(f"A quantidade de palavras é: {quantidade}")
    