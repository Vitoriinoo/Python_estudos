while True:
    mes = int(input("Digite o número do mês (1-12): "))

    match mes:
        case 12 | 1 | 2:
            print("Verão")
            break

        case 3 | 4 | 5:
            print("Outono")
            break

        case 6 | 7| 8:
            print("inverno")
            break

        case 9 | 10 | 11:
            print("Primavera")
            break
    
        case _:
            print("Mês inválido. Tente novamente.")
            

        