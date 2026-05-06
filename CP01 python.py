# ====================================== EX01 ======================================
# Crie um programa em Python que verifique se uma pessoa pode entrar em um evento 
# se for maior de 18 anos.
while True:

    i = int(input("Digite a sua idade: "))

    if i >= 18 and i <100:
        print("Acesso liberado ao evento")
        break

    elif i < 18 and i >= 0:
        print("Acesso negado, evento permitido apenas para maiores de idade")
        break
    
    else:
        print("O valor digitado não corresponde a uma idade válida(0/100), tente novamente.")
# ==================================== FIM EX01 ====================================

# ====================================== EX02 ======================================
# Crie um programa em Python que compare dois números, peça ao usuario os numeros e
# compare se eles são iguais.
numeros = []

for i in range(2):
    i = float(input(f"Digite o {i+1}° número: "))
    numeros.append(i)

if numeros[0] == numeros[1]:
    print(f"OS números são iguais.")

else:
    print(f"Os números são diferentes.")
# ==================================== FIM EX02 ====================================

# ====================================== EX03 ======================================
# Crie um programa em Python que registre 3 notas de um aluno e determine 
# sua situação na disciplina, peça ao usuario as 3 notas e salve em uma lista, tire 
# a media e se for 7 ou maior ele passou na materia.
lista_notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}º nota: "))
    lista_notas.append(nota)

soma_notas = sum(lista_notas)
quantidade = len(lista_notas)

if soma_notas / quantidade >= 7:
    print(f"Você passou na matéria")

else:
    print(f"Você não passou na metéria")
# ==================================== FIM EX03 ====================================

# ====================================== EX04 ======================================
# Crie um programa em Python que registre 5 produtos comprados em um mercado. 
# Use Listas, laço for e inputs.
compras = []

for i in range(5):
    produtos = input(f"Digite o nome do {i+1}º produto: ")
    compras.append(produtos)

print(f"Produtos comprados:\n{compras}")
# ==================================== FIM EX04 ====================================

# ====================================== EX05 ======================================
# Crie um programa em Python que registre 5 números digitados pelo usuário e 
# depois mostre algumas informações sobre eles, use laço For.
# 1 - A lista completa de números
# 2 - O maior número
# 3 - O menor número
# 4 - A soma de todos os números
lista_numeros = []

for i in range(5): 
        numeros_solicitados = float(input(f"Digite o {i+1}º número: "))
        lista_numeros.append(numeros_solicitados)


print(f"Lista completa: {lista_numeros}")
print(f"Maior número: {max(lista_numeros)}")
print(f"Menor número: {min(lista_numeros)}")
print(f"Soma de todos os números: {sum(lista_numeros)}")
# ==================================== FIM EX05 ====================================

# ====================================== EX06 ======================================
# Crie um programa em Python que peça números ao usuário e some todos eles.
# Use o laço while e receba numeros ate que uma condição seja atendida.
soma_total = 0

while True:
    numero = float(input("Digite um número para ser adicionado (ou -1 para parar): "))
    
    if numero == -1:
        break
        
    soma_total += numero

print(f"Condição de parada atendida. A soma final de todos os números válidos foi: {soma_total}.")
# ==================================== FIM EX06 ====================================

# ====================================== EX07 ======================================
# Crie um programa em Python que simule um sistema simples de login.
# Usar um primeiro laço while para pedir o nome de usuário até que 
# o usuário digite o valor correto, faça o mesmo para a senha.
nome_usr = input("Digite o seu nome de usuário: ")
senha_usr = input("Digite a sua senha: ")

print("Para realizar seu acesso, digite o que for solicitado: ")


verificacao_nome = input("Digite seu nome de usuário: ")
verificacao_senha = input("Digite a sua senha: ")

while verificacao_nome != nome_usr or verificacao_senha != senha_usr:
        print("Nome de usuário e/ou senha incorreto. Verifique e tente novamente.")
        verificacao_nome = input("Digite seu nome de usuário: ")
        verificacao_senha = input("Digite a sua senha: ")
        break


print("Acesso concedido")
# ==================================== FIM EX07 ====================================

# ====================================== EX08 ======================================
# Crie um programa em Python que registre 3 notas de alunos, garantindo que 
# cada nota seja válida, use as estruturas de laço for e while.
notas = []

for i in range(3):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")
print(f"Notas registradas: {notas}")
# ==================================== FIM EX08 ====================================

# ====================================== EX09 ======================================
# Crie um programa em Python que registre números digitados pelo usuário e 
# conte quantos são positivos. Use o laço while para registrar todas as entradas
# depois use o laço for para percorrer toda a lista e fazer a contagem.

# ==================================== FIM EX09 ====================================
lista_nums = []

while True:
    nums = float(input("Digite um número (digite 0 para parar): "))

    if nums == 0:
        break
    lista_nums.append(nums)

nums_positivos = 0

for num in lista_nums:
    if num > 0:
        nums_positivos += 1

    print(f"A quantidade de números postivos: {nums_positivos}")
# ====================================== EX10 ======================================
# Crie um programa em Python que registre as notas de 3 alunos em 4 provas usando
# uma matriz (lista de listas), calcule a media de cada aluno.
# Use seu conhecimento de laços para cumprir a tarefa.
notas = []

for i in range(3): 
    aluno = []
    
    for j in range(4):  
        nota = float(input(f"{i+1}º aluno, {j+1} ª prova. A nota foi: "))
        aluno.append(nota)
    
    notas.append(aluno)

for i in range(3):
    soma = 0
    
    for j in range(4):
        soma += notas[i][j]
    
    media = soma / 4
    print(f"Média do aluno {i+1}: {media}")
# ==================================== FIM EX10 ====================================
