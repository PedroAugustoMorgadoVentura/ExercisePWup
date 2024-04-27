def lista_ordenada(a):
    a.sort()
    return max(a)
lista = []
for i in range(0,3):
    x = int(input("Digite um número na lista: "))
    lista.append(x)


lista_maior = lista_ordenada(lista)

print(f"Aqui está a maior lista: {lista_maior}")






