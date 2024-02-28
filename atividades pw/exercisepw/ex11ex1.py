a = float(input("Digite o 'a' da equação:  "))
b = float(input("Digite o 'b' da equação:  "))
c = float(input("Digite o 'c' da equação:  "))

print(f"A função do segundo grau está escrita como: {a}x² + {b}x + {c}  =  0")
delta = (b**2) - (4*a*c)
x1 = (-b + delta**(1/2)) / (2*a)
x2 = (-b - delta**(1/2)) / (2*a)

print(f"A primeira raiz da função vale {x1} e a segunda raiz da função vale {x2}")
