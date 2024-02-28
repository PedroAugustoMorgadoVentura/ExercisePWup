numeros = input("Digite uma lista de números separados por espaços: ").split()
numeros_invertidos = [numeros[i] if i % 2 != 0 else numeros[-i - 1] for i in range(len(numeros))]
print("Lista com os elementos de índices pares invertidos:", numeros_invertidos)
