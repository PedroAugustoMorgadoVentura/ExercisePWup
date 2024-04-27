class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura
    

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


lado = Quadrado(5)

print(lado.area())
        