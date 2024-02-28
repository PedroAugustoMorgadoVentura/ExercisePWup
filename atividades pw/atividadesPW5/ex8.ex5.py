numeros = []

for i in range(0,10):
    num = int(input("Digite um número: "))
    numeros.append(num)

quadrados = map(lambda x: x**2, numeros)

print(list(quadrados))