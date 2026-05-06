palavra = str(input("Digite uma palavra: "))
vogais = ["A" , "a" , "E" , "e" , "I" , "i" , "O" , "o" , "U" , "u"]
def cont_vogais(palavra):
    contador = 0
    for letras in palavra:
        if letras in vogais:
         contador += 1
    return contador

total = cont_vogais(palavra)
print(f"A quantidade de vogais na sua palavra é: {total}")
    

