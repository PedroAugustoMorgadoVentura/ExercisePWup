numeros = []
for x in range(1,21):
    numeros.append(x)

quadrados = [x**(1/2) for x in numeros if x%2 == 0]

print(quadrados)