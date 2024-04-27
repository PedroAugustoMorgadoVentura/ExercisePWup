class ValorNegativoError(Exception):
    """Exceção personalizada para representar valores negativos."""

    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem

def calcular_raiz_quadrada(numero):
    if numero < 0:
        raise ValorNegativoError("O número não pode ser negativo.")
    else:
        return numero ** 0.5

# Exemplo de uso
try:
    resultado = calcular_raiz_quadrada(-5)
except ValorNegativoError as e:
    print("Erro ao calcular a raiz quadrada:", e.mensagem)
