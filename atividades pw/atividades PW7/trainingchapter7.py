import zipfile
import os

# Diretório a ser adicionado ao arquivo ZIP
diretorio_a_zipar = 'caminho/do/seu/diretorio'

# Nome do arquivo ZIP a ser criado
nome_arquivo_zip = 'meuzippzinho.zip'

# Criar o arquivo ZIP
with zipfile.ZipFile(nome_arquivo_zip, 'w') as meu_zip:
    # Adicionar o conteúdo do diretório ao arquivo ZIP
    for pasta_raiz, pastas, arquivos in os.walk(diretorio_a_zipar):
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta_raiz, arquivo)
            meu_zip.write(caminho_completo, os.path.relpath(caminho_completo, diretorio_a_zipar))

# Agora, abrir o arquivo ZIP para extração (se necessário)
with zipfile.ZipFile(nome_arquivo_zip, 'r') as meu_zip:
    meu_zip.extractall('meudiretorio')
