numeros = input("Digite uma lista de números separados por espaços: ").split()
numero_referencia = float(input("Digite um número de referência: "))
posicao = next((i for i, num in enumerate(numeros) if float(num) > numero_referencia), None)
print("Posição do primeiro elemento maior que o número de referência:", posicao)
