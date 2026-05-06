matriz = [   
    [1, 2],
    [4, 5]
]
variavel_escalar = 3
matriz2 = []

for i in range(2):
    linha = []

    for j in range(2):
        linha.append(matriz[i][j] * variavel_escalar)
    matriz2.append(linha)

for linha in matriz2:
    print(linha)

