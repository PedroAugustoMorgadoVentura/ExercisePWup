def escrever_arquivo(nome_arquivo, dados):
    arquivo = None
    try:
        arquivo = open(nome_arquivo, 'w')  # Abre o arquivo para escrita
        arquivo.write(dados)  # Escreve os dados no arquivo
        print("Dados escritos no arquivo com sucesso.")
    except IOError:
        print("Erro: Falha ao escrever no arquivo.")
    finally:
        if arquivo is not None:
            try:
                arquivo.close()  # Fecha o arquivo
                print("Arquivo fechado.")
            except IOError:
                print("Erro ao fechar o arquivo.")

# Exemplo de uso
dados = "Exemplo de dados a serem escritos no arquivo."
escrever_arquivo("exemplo.txt", dados)
