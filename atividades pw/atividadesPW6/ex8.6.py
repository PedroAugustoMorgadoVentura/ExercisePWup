def inverso(a):
    inverso = a[::-1]
    return inverso


frase = input("Digite uma frase: ")


frase_invertida = inverso(frase)

print(frase_invertida)