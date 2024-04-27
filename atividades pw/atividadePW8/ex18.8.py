class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico do animal")


class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")


cachorro = Cachorro("Rex")
cachorro.emitir_som()
