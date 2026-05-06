while True:
    idade = int(input("Digite a sua idade: "))

    match idade:
        case idade if idade <= 12:
                print("Criança")
                break

        case idade if idade <= 17 and idade > 12:
                print("Adolescente")
                break
        
        case idade if idade == 18 and idade < 100:
                print("Adulto")
                break
        
        case _:
                print("Idade inválida, tente novamente")
            

        
