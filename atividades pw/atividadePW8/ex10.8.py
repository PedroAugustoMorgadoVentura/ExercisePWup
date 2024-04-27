class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def mostrardados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}")

class Cliente(Pessoa):
    def __init__(self, nome, idade, endereço):
        super().__init__(nome, idade)
        self.endereço = endereço
    
    def mostrardados(self):
        super().mostrardados()
        print(f"Endereço: {self.endereço}")

cliente = Cliente('Pedro', 19, 'rua Coimbra')
cliente.mostrardados()
