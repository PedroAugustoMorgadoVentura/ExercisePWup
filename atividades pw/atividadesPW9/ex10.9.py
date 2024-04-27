class MeuErro(Exception):
    """Exceção personalizada para representar um erro específico."""

    def __init__(self, mensagem):
        super().__init__(mensagem)  # Chama o construtor da classe base
        self.mensagem = mensagem

# Exemplo de uso da exceção personalizada
def checar_numero(numero):
    if numero < 0:
        raise MeuErro("O número não pode ser negativo.")

# Testando a exceção personalizada
try:
    checar_numero(-5)
except MeuErro as e:
    print("Erro:", e.mensagem)
