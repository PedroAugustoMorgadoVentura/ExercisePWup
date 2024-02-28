import re
frase = str(input("Digite uma frase: "))

palavras  = frase.split(" ")

trade_to_o = [palavra.replace("a","o") for palavra in palavras]


print(trade_to_o)