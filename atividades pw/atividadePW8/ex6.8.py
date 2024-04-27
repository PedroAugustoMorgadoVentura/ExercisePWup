from math import pi
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        area = pi*self.raio*self.raio
        print(f"Área do círculo: {area}")



instancia = Circulo(int(input("Digite o valor do raio: ")))
instancia.area()
        