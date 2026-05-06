while True:
    i = float(input("Digite a sua nota: "))

    match i:
        case i if i >= 9 and i <= 10:
            print("Excelente")
            break

        case i if i >= 7 and i < 9:
            print("Bom")
            break

        case i if i >= 5 and i <= 6:
            print("Regular")
            break

        case i if i < 5 and i >=0:
            print("Reprovado")
            break

        case i if i <0:
            print("Nota inválida, tente novamente")

    
        case _:
            print("Nota inválida, tente novamente")

        

    

    
