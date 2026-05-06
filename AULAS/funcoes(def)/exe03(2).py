semestre = []
lista = []

def calcularMedia(lista):
    return sum(lista) / len(lista)

print("lista de notas bimestrais")

for i in range(2):
    lista = []
    while True:
        print(f" {i+1} - Bimestre")
        nota = float(input("Digite uma nota a ser inserida no sistema para calcular a média (digite -1 para parar o programa) "))
        if nota < 0:
            break
        lista.append(nota)
        print(f"Média até o momento: {calcularMedia(lista)}")
    print(f"A média do {i+1}° bimestre: {calcularMedia(lista)}")
    semestre.append(lista)

for i in semestre:
    print(i)