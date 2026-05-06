msg = ''' 
1 - Domingo
2 - Segunda-feira
3 - Terça-feira
4 - Quarta-feira
5 - Quinta-feira
6 - Sexta-feira 
7 - Sábado

'''


while True:

    dia = int(input(f"{msg}Digite o número do dia da semana: "))

    match dia:
        case 1:
            print("Domingo")
            break
        case 2: 
            print("Segunda-feira")
            break
        case 3:
            print("Terça-feira")
            break
        case 4:
            print("Quarta-feira")
            break
        case 5:
            print("Quinta-feira")
            break
        case 6:
            print("Sexta-feira")
            break
        case 7:
            print("Sábado")
            break
        case _:
            print("Dia inválido, tente novamente")