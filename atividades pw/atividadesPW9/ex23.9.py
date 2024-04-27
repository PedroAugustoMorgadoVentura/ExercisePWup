try:
    with open("numeros.txt", "r") as arquivo:
        numeros = [int(numero) for numero in arquivo.readlines()]
        print("Soma dos números:", sum(numeros))
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except ValueError:
    print("Erro: Valor inválido no arquivo.")
