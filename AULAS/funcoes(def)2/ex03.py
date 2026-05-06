def soma_algarismos(numero):
    numero_texto = str(numero)
    soma = 0
    
    for digito in numero_texto:
        soma += int(digito)
        
    return soma

n = int(input("Digite um número: "))
resultado = soma_algarismos(n)

print(f"A soma de {n} (algarismo por algarismo) é: {resultado}")



