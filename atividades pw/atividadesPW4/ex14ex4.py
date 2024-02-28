frase = input("Digite uma frase: ")

palavras = frase.split()

print("Posição inicial de cada palavra na frase:")
for palavra in palavras:
    posicao_inicial = frase.find(palavra)
    print(f"A palavra '{palavra}' começa na posição {posicao_inicial}")
