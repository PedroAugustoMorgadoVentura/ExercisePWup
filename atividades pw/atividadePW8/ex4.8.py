class Carro:
    def __init__(self, speed):
        self.speed = speed

    def acelerar(self, tempo):
        aceleração = 10
        velocidademaxima = aceleração*tempo
        self.speed += velocidademaxima

    def frear(self, tempo):
        freio = 5
        freiomaximo = freio*tempo
        self.speed -= freiomaximo

    def exibir(self):
        print(f"Velocidade final do carro: {self.speed}m/s")


Instancia = Carro(10)

Instancia.acelerar(int(input("Qual o tempo de aceleração que você deseja?" )))
Instancia.frear(int(input("Por quanto tempo vc quer que o carro freie? ")))
Instancia.exibir()

