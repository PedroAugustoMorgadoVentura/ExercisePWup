def calcular_media(lista):
    if not lista:
        raise ValueError("A lista está vazia.")
    return sum(lista) / len(lista)
