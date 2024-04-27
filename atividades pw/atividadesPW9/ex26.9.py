def calcular_media(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        raise ValueError("A lista não pode estar vazia.") from None


def main():
    lista_numeros = [10, 20, 30, 40, 50]

    try:
        resultado = calcular_media(lista_numeros)
        print("Média dos números:", resultado)
    except ValueError as e:
        print("Erro ao calcular a média:", e)

if __name__ == "__main__":
    main()
