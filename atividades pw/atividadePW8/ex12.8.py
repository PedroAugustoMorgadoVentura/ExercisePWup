class Veiculo:
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def frear(self, freio, tempo):
        decremento = freio*tempo
        if self.velocidade > 0:
            self.velocidade -= decremento
        else:

            print("Velocidade está em 0")
    def aceleracao(self, acelerar, tempo):
        incremento = acelerar*tempo
        self.velocidade += incremento

class Carro(Veiculo):
    def __init__(self, velocidade, marca):
        super().__init__(velocidade)
        self.marca = marca
    def mostrardados(self):
        print(f"Marca: {self.marca}")
        print(f"velocidade: {self.velocidade}")


velocidade = int(input("Digite a speed inicial do carro: "))
tempo = int(input("Digite o tempo que você quer que o carro freie ou acelere:"))
marca = str(input("Digite a marca do carro: "))


carro = Carro(velocidade, marca)
carro.mostrardados()
aceleracao = int(input("Digite a aceleracao do carro: "))
carro.aceleracao(aceleracao, tempo)
carro.mostrardados()
freio = int(input("Digite o quanto  você quer que o carro freio por segundo: "))
carro.frear(freio, tempo)
carro.mostrardados()

    
    
