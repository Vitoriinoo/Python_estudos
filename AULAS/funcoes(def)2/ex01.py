def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1  #APENAS PARA O 2º TERMO, POIS O 1º É 0 E O 2º É 1
    
    a = 0
    b = 1
    
    #Começamos a contar a partir do 3º termo, pois os anteriores ja foram resolvidos
    for i in range(3, n + 2):
        proximo = a + b
        a = b
        b = proximo
        
    return b #vai retornar o próximo vsalor

# Teste
posicao = int(input("Digite a posição do número de Fibonacci que deseja calcular: "))
print(f"O {posicao}º número de Fibonacci é: {fibo(posicao)}")