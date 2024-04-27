try:
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
