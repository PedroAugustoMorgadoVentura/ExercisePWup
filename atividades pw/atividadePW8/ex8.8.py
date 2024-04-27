class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrardados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}")
        
        

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    def mostrardados(self):
        
        print(f"Nome: {self.nome} \nIdade: {self.idade} \nMatricula: {self.matricula}")


Instancia = Aluno('pedro', 19, '20211imi013')

Instancia.mostrardados()