class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente ou valor de saque inválido.')

    def consultar_saldo(self):
        print(f'Saldo atual: R$ {self.saldo:.2f}')


class ContaPoupanca(ContaBancaria):
    def __init__(self, taxa_juros):
        super().__init__()
        self.taxa_juros = taxa_juros

    def rendimento(self):
        rendimento_mensal = self.saldo * (self.taxa_juros / 100)
        self.depositar(rendimento_mensal)
        print(f'Rendimento mensal: R$ {rendimento_mensal:.2f}')

conta_poupanca = ContaPoupanca(0.5)

conta_poupanca.depositar(1000)

conta_poupanca.rendimento()
