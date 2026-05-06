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

pessoa1 = Pessoa("Vitor", 18, 63, 1.75, "Masculino")

pessoa1.envelhecer()

pessoa1.descrever()

#3. Crie um novo método na classe Pessoa chamado envelhecer que vai adicionar mais um ano a idade da pessoal.





                                                 
                                                                