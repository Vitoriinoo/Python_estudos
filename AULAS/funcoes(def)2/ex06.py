def maisusculas(frase):
    frase_maiuscula = frase.upper()
    return frase_maiuscula

frase = input("Digite uma frase: ")
resultado = maisusculas(frase)
print(f"A frase em maiúsculas é: {resultado}")