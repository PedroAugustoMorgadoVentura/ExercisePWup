while True:
    try:
        nome_arquivo = input("Digite o nome do arquivo: ")
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
        break
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
