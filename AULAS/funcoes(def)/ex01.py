opcao = int(input("Digite uma opção: \n 1 - Adição  \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n :"))

num = float(input("Digite um número: "))
num2 = float(input("Digite o segundo número: "))

def adicao(num, num2):
    
    return num + num2


def subtracao(num, num2):
    
    return num - num2
    

def multiplicacao(num, num2):
    
    return num * num2
  


def divisao(num, num2):
    if num == 0 or num2 == 0:
        print("Impossivel dividir por zero seu usuário")
        return None
    return num / num2
    

match opcao: 
    case 1:
        soma = adicao(num, num2)
        print(f"O resultado da soma é: {soma}")

    case 2:
        subtra = subtracao(num, num2)
        print(f"O resultado da subtração é: {subtra}")

    case 3:
        multi = multiplicacao(num, num2)
        print(f"O resultado da multiplicação é: {multi}")

    case 4: 
        divi = divisao(num, num2)
        print(f"O resultado da divisão é: {divi}")



