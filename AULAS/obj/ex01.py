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

#Criar uma Classe Pessoa: Crie uma classe chamada Pessoa com os atributos nome, idade, peso, altura e sexo. Adicione um método descrever que retorna uma string com os atributos da pessoa.



                                                 
                                                                