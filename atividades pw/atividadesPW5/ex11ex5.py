numeros = input("Digite um ou vários números:").split(" ")

pares = [int(numero) for numero in numeros if int(numero) % 2 == 0]


print(pares)
