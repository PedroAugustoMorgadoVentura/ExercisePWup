class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def emitir_som(self):
        print(f"{self.nome} fez um som genérico. ")
    


dogao = Animal('Rex', 5)
dogao.emitir_som()

    