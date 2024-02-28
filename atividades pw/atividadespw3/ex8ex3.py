def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

try:
    numero = int(input("Digite um número para calcular o fatorial: "))
    if numero < 0:
        print("O fatorial de números negativos não é definido.")
    else:
        resultado = fatorial(numero)
        print(f"O fatorial de {numero} é {resultado}.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
