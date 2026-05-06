matriz = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

del matriz[1]

print("Matriz após a remoção da segunda linha: ")
for linha in  matriz:
    print(linha)

elemento = matriz[0].pop(2)
print("\nElemento removido:", elemento)

print("\nMatriz após a remoção do elemento: ")
for linha in matriz:
    print(linha)