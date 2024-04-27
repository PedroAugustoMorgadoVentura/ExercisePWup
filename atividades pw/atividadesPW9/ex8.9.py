def ler_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'r')
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:", conteudo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except IOError:
        print("Erro: Falha ao ler o arquivo.")
    finally:
        try:
            arquivo.close()  # Tentativa de fechar o arquivo
        except UnboundLocalError:
            pass  # Ignorar erro se o arquivo não foi aberto com sucesso

# Exemplo de uso
ler_arquivo("arquivo.txt")
