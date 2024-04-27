class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3


class TrianguloRetangulo(Triangulo):
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2, lado3)

    def area(self):
        semiperimetro = self.perimetro() / 2
        area = (semiperimetro * (semiperimetro - self.lado1) *
                (semiperimetro - self.lado2) * (semiperimetro - self.lado3)) ** 0.5
        return area


triangulo_retangulo = TrianguloRetangulo(3, 4, 5)
print("Perímetro:", triangulo_retangulo.perimetro())
print("Área:", triangulo_retangulo.area())
