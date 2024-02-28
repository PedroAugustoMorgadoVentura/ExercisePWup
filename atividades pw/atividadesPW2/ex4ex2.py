ano = int(input("Digite um número: "))
x = "bissexto" if ano%4 == 0 and ano%100 != 0 else "Não é bissexto"
print(x)