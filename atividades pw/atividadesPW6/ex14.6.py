def lista():
    lista = []
    choice = int(input("Digite até o número que você quer que a lista vá: "))
    for i in range(0, choice+1):
        lista.append(i)
    return lista

def bigger_than(minimo):
    def condicao(numero):
        return numero > minimo
    return condicao

def intersection(lista, bigger):
    return [element for element in lista if bigger(element)]

print(intersection(lista(), bigger_than(int(input("Digite o tamanho mínimo do número para ele aparecer na lista: ")))))
