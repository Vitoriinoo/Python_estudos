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

pessoa1.descrever()
pessoa2.descrever()

pessoa1.envelhecer()
pessoa2.envelhecer() 

pessoa1.comparar_idade(pessoa2)

# Comparar Idades: Crie um método na classe Pessoa chamado comparar_idade que recebe outra pessoa como parâmetro e retorna se a pessoa é mais velha, mais nova ou tem a mesma idade que a pessoa atual



                                                 
                                                                