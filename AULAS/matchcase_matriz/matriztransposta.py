notas = [
    [8, 7], # Aluno 0
    [9, 5], # Aluno 1
    [6, 8], # Aluno 2
    [10, 4] # Aluno 3
]

notasnovas = []

for i in range(2):
    linha_nova = []

    for j in range(4):
        linha_nova.append(notas[i][j])
        notasnovas.append(linha_nova)

for linha_nova in notasnovas:
    print(linha_nova)

        