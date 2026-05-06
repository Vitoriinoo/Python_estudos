matriz = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

nova_linha = [10, 11, 12]

matriz.append(nova_linha)

matriz[1].insert(0, 100)



for linha in matriz:
    print(linha)
