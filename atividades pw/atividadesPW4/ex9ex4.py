frase = input("Digite uma frase: ")
palavra_presente = input("Digite uma palavra presente na frase: ")
palavra_ausente = input("Digite uma palavra ausente na frase: ")

nova_frase = frase.replace(palavra_presente, palavra_ausente)

print("Nova frase:")
print(nova_frase)
