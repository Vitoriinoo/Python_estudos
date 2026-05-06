peso1 = 5
peso2 = 7
peso3 = 10

def calcular_media_ponderada(nota1, nota2, nota3):
    ponderado = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)

    media_ponderada = ponderado / 3
    return media_ponderada


nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

print(f"A média ponderada das notas enviadas é: {calcular_media_ponderada(nota1, nota2, nota3):.2f}")