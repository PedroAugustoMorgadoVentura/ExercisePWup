palavra = input("Digite uma palavra que tenha um palíndromo: ")
palíndromo = palavra[::-1]
if palíndromo == palavra:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")