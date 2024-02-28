frase = input("Digite uma frase: ")

for i in range(0, len(frase), 6):
    print(frase[i:i+6])
