while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero < 0:
            raise ValueError("O número não pode ser negativo.")
        raiz = numero ** 0.5
        print("A raiz quadrada de", numero, "é:", raiz)
        break
    except ValueError as e:
        print("Erro:", e)
