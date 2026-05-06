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

pessoa1.descrever()

#Criar um Objeto Pessoa: Crie um objeto da classe Pessoa com o seu nome e demais atributos. Use o método descrever para imprimir as informações do objeto.


                                                 
                                                                