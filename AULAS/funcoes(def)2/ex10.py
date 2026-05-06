def lista_primos(n):
    primos = [] 
    
    for num in range(2, n + 1):
        eh_primo = True 
        
        for i in range(2, num):
            if num % i == 0:
                eh_primo = False  
                break  
        
        if eh_primo:
            primos.append(num) 
            
    return primos

# Teste
limite = int(input("Até qual número você quer buscar primos? "))
print(f"Primos até {limite}: {lista_primos(limite)}")