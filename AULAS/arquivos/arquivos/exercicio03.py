palavra = input("Digite a palavra que deseja conferir: ")
linha_atual = 0  
achei = False
with open('ambos.txt', 'r', encoding='UTF-8') as file:
    for linha in file:
        linha_atual += 1  # Soma 1 toda vez que entra em uma nova linha
        
        if palavra in linha:
            print(f"A palavra '{palavra}' está na linha {linha_atual}")
            achei = True
    if achei == False:
        print(f"A palavra {palavra} não foi encontrada no arquivo")
