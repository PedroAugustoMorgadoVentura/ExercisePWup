arquivo = open('meuarquivo.txt', 'w')
arquivo.write('Este é o conteúdo do meu arquivo.')
arquivo.close()



arquivo = open("meuarquivo.txt", "r")
linha = arquivo.readline()
while linha:
    print(linha)
    linha = arquivo.readline()

arquivo.close

