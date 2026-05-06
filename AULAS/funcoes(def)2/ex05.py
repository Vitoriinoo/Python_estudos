def eh_palindromo(texto):
    # Remove espaços e coloca em minúsculo
    texto = texto.replace(" ", "").lower()
    
    # Inverte e compara
    return texto == texto[::-1]

# Teste
entrada = input("Digite uma palavra ou frase: ")

if eh_palindromo(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")