chaves = input("Digite uma lista de chaves separadas por espaços: ").split()
valores = input("Digite uma lista de valores separados por espaços: ").split()

# Verifica se o número de chaves é igual ao número de valores
if len(chaves) != len(valores):
    print("O número de chaves e valores não é o mesmo.")
else:
    dicionario = dict(zip(chaves, valores))
    print("Dicionário resultante:", dicionario)
