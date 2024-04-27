class ErroEspecifico(Exception):
    """Exceção personalizada para um erro específico."""
    def __init__(self, mensagem):
        super().__init__(mensagem)

def funcao_com_erro():
    try:
        # Simulando um erro específico
        raise ErroEspecifico("Ocorreu um erro específico na função.")
    except ErroEspecifico as e:
        # Tratamento do erro específico
        print("Erro específico:", e)
        # Encadeando para uma exceção genérica
        raise Exception("Ocorreu um erro genérico.") from e

# Exemplo de uso
try:
    funcao_com_erro()
except Exception as e:
    print("Erro genérico:", e)
