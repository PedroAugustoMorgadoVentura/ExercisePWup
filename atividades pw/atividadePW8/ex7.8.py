class Pessoa: 
    def __init__(self, nome, idade ):
        self.nome = nome
        self.idade = idade

    def mostrardados(self):
        print(f"Nome: {self.nome} \n Idade: {self.idade} anos")
    

class Funcionario(Pessoa):
    def __init__(self,nome, idade,  salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def mostrardados(self):
         print(f"Nome: {self.nome} \n Idade: {self.idade} anos \n Salario: R${self.salario},00")



lista = [Pessoa('Pedro',4), Pessoa('Joao',5), Funcionario('Lucas',20,10000), Funcionario('Jose',18,2000)]

for objeto in lista:
    objeto.mostrardados()