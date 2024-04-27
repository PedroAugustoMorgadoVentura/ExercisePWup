class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def mostrar_dados(self):
        print(f"Aqui está o nome de {self.nome} e idade {self.idade}")


instancia1 = Pessoa('José', 20)
instancia2 = Pessoa('Maria', 9)


instancia1.mostrar_dados()
instancia2.mostrar_dados()
        