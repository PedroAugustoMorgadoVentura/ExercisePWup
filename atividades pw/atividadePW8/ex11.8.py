class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def mostrardados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade,salario):
        super().__init__(nome, idade)
        self.salario = salario

    def aumentarsalario(self, percentual):
        aumento = self.salario * (percentual/100)
        self.salario += aumento

    def mostrardados(self):
        super().mostrardados()
        print(f"Salario: {self.salario}")
funcionario = Funcionario('Pedro', 19, 3600)
funcionario.mostrardados()
funcionario.aumentarsalario(10)
funcionario.mostrardados()