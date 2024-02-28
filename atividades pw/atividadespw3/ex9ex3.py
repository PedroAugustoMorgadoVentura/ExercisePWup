numeros = []
divisivel3 = []
divisivel5 = []
for i in range(1,101):
    numeros.append(i)

for exam in numeros:
    if exam%3 == 0:
        divisivel3.append(exam)
    elif exam%5 == 0:
        divisivel5.append(exam)
    else:
        continue


print(f"Aqui está a lista de números divisíveis por 3 de 1 a 100: {divisivel3}. \n Aqui está a lista de números divisíveis por 5 de 1 a 100: {divisivel5}")
