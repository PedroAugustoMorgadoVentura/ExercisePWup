palavra = str(input("Digite uma palavra: "))
palíndromo = "É um palíndromo" if palavra[::-1] == palavra else "Não é palíndromo"
print(palíndromo)