lista1 = input("Digite a primeira lista de números separados por espaços: ").split()
lista2 = input("Digite a segunda lista de números separados por espaços: ").split()
media = [(float(lista1[i]) + float(lista2[i])) / 2 for i in range(len(lista1))]
print("Médias dos elementos correspondentes:", media)
