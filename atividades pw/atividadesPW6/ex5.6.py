def imprimir_x():
    x = 10
    print("O valor de x dentro da função é:", x)
imprimir_x()

try:
    print("O valor de x fora da função é:", x)
except NameError:
    print("Erro: A variável 'x' não está definida fora da função.")
#Para funcionar precisa do return, como será mostrado no ex5.6.6