palavras = str(input("Digite uma ou várias palavras:")).split(" ")
comprimentos = []


for palavra in palavras:
    comprimentos.append(len(palavra))
print(palavras, comprimentos)
