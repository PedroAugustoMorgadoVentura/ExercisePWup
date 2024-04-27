intersection = lambda list1, list2: [num for num in list2 if num in list1]

lista1 = []
lista2 = []

print("Se deseja interromper, digite k")
while True:
    num = input("Digite um número na lista 1: ")
    
    if num == "k":
        break
    lista1.append(int(num))

    num = input("Digite um número na lista 2: ")
    
    if num == "k":
        break
    lista2.append(int(num))
    

resultado = intersection(lista1, lista2)


print("Resultado da interseção: ", resultado)