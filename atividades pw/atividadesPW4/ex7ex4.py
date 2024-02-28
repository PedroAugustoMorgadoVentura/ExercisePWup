import re

def limpar_input(input_str):
    return re.sub(r'[^a-zA-Z0-9]', '', input_str)

usuario = input("Digite um nome de usuário: ")
usuario_limpo = limpar_input(usuario)
print("Nome de usuário limpo:", usuario_limpo if usuario != usuario_limpo else "Nome de usuário válido:", usuario)

senha = input("\nDigite uma senha: ")
senha_limpa = limpar_input(senha)
print("Senha limpa:", senha_limpa if senha != senha_limpa else "Senha válida:", senha)
