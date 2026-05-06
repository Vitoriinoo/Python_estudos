i = int(input("Digite um numero para sabermos se ele é primo: "))

def primo(i):
    eh_primo = True
    for j in range(2,i):
        if i % j == 0:
            eh_primo = False
    return eh_primo

print(primo(i))
