artigos = ["o", "a", "os", "as", "um", "uma", "uns", "umas"]

frase = input("Digite uma frase: ")

palavras = frase.split()

frase_sem_artigos = " ".join(palavra for palavra in palavras if palavra.lower() not in artigos)

print("Frase sem os artigos:")
print(frase_sem_artigos)
