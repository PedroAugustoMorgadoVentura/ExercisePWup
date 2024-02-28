frase = input("Digite uma frase: ")

palavras = frase.split()

for i in range(len(palavras)):
    palavras[i] = palavras[i].strip()

frase_sem_espacos_desnecessarios = ' '.join(palavras)

print("Frase com espaços desnecessários removidos:")
print(frase_sem_espacos_desnecessarios)
