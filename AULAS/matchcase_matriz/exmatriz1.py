matriz = [   
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz3 = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz[i][j] + matriz2[i][j])
    matriz3.append(linha)

for linha in matriz3:
    print(linha)