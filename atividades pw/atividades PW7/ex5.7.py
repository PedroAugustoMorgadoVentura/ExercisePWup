import os

def remove(file):
    return os.remove(file)



file = input("Escreva o arquivo que quer deletar: ")

remove = remove(file)

