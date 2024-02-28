numeros = []
primos = []


for i in range(1, 101):
    numeros.append(i)


for num in numeros:

    if num < 2:
        continue

    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        primos.append(num)

print("Números primos de 1 a 100:", primos)
