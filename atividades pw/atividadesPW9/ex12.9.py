class MeuErroPersonalizado(Exception):
    """Exceção personalizada para representar um erro específico."""

    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem

# Exemplo de uso da exceção personalizada
def verificar_idade(idade):
    if idade < 18:
        raise MeuErroPersonalizado("Você precisa ter pelo menos 18 anos para acessar este conteúdo.")

# Testando a exceção personalizada
try:
    verificar_idade(15)
except MeuErroPersonalizado as e:
    print("Erro:", e.mensagem)
