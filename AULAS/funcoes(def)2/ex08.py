vogais = "A","E","I","O","U","a","e","i","o","u"

def contar_vogais(frase):
        contador = 0

        for letra in frase:
            if letra in vogais:
                contador += 1

        return contador

frase = input("Digite uma frase: ")
print(f"A quantidade de vogais na sua frase é: {contar_vogais(frase)}")