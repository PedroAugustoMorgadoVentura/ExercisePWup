while True:
    frase = input("Digite uma frase com 5 palavras: ")
    palavras = frase.split()
    if len(palavras) == 5:
        break
    else:
        print("A frase digitada não possui 5 palavras. Tente novamente.")

print("\nPalavras na frase:")
for palavra in palavras:
    print(palavra)
