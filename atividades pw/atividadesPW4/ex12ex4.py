frase = input("Digite uma frase: ")

palavras = frase.split()

terminam_com_o = 0
terminam_com_a = 0

for palavra in palavras:
    if palavra.endswith('o'):
        terminam_com_o += 1
    elif palavra.endswith('a'):
        terminam_com_a += 1

print("Palavras que terminam com 'o':", terminam_com_o)
print("Palavras que terminam com 'a':", terminam_com_a)
