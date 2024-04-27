class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def sacar(self):
        valor = int(input("Quanto deseca sacar da conta(R$)? "))
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("O PS5 não vem hoje amigão")
    def depositar(self):
        valor = int(input("Quanto deseja depositar(R$)? "))
        self.saldo += valor
    
    def exibir(self):
        print(f"Aqui está o saldo da conta: R${self.saldo},00")


instancia = ContaBancaria(500)
instancia.sacar()
instancia.depositar()
instancia.exibir()