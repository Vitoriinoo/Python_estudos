class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
    
    def descrever(self):
        atributos_pessoa = (
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Peso: {self.peso}\n"
            f"Altura: {self.altura}\n"
            f"Sexo: {self.sexo}"
            )
        
        print(atributos_pessoa)

    def envelhecer(self):
        self.idade = self.idade + 1

    def comparar_idade(self, outra_pessoa):
        if self.idade > outra_pessoa.idade:
            print(f"{self.nome} é mais velho(a).")
        elif self.idade < outra_pessoa.idade:
            print(f"{self.nome} é mais novo(a).")
        else:
            print(f"Ambos têm a mesma idade.")

pessoa1 = Pessoa("Vitor", 18, 63, 1.75, "Masculino")

pessoa2 = Pessoa("Silvio", 19, 73, 1.80, "Masculino")

pessoa3 = Pessoa("Janete", 71, 69, 1.59, "Feminino")

pessoa4 = Pessoa("Luana", 27, 75, 1.72, "Feminino")

pessoa5 = Pessoa("Malon", 23, 82, 1.82, "Masculino")

pessoa6 = Pessoa("Mario", 65, 78, 1.79, "Masculino")

pessoa7 = Pessoa("Julia", 18, 61, 1.60, "Feminino")

lista_de_pessoas = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5, pessoa6, pessoa7]

print("RELATÓRIO GERAL DE PESSOAS")
for p in lista_de_pessoas:
    p.descrever()
    print("-" * 20)

# 5. Criar uma Lista de Pessoas: Crie uma lista de objetos. Pessoa com diferentes nomes e idades. Use um loop para percorrer a lista e imprimir as informações de cada pessoa.





                                                 
                                                                