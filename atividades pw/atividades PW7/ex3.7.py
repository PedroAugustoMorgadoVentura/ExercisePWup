entrada = input("O arquivo de entrada(digite a extensão também): ")
saida = input("O arquivo de saída: ") 



with open(entrada, "r") as file:
 linhas = file.readlines()
 inverted_lines = [linha[::-1]+ "\n" for linha in linhas]



with open(saida, "w") as saida:
 saida.writelines(inverted_lines)


print("Tudo feito")
