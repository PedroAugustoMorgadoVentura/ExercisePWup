numeros = []
for x in range(1,11):
    numeros.append(x)

quadrados = [x**(2) for x in numeros if x%2 == 0]

print(quadrados)