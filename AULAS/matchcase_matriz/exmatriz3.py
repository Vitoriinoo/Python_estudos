#MATRIZ TRANSPOSTA

matriz = [
    [1,2],
    [3,4],
    [5,6]
]

transposta = []

for j in range(2):
    linha_nova = []

    for i in range(3):
        linha_nova.append(matriz[i][j])
    transposta.append(linha_nova)

print("A matriz transposta (2x3)")
for linha in transposta:
    print(linha)
