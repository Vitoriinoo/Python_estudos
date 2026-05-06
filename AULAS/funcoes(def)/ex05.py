n = int(input("Digite um número para descobrir seu fatorial: "))

def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

print(f"O fatorial do {n} é {fatorial(n)}")