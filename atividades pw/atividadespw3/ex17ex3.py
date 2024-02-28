números = []

for i in range(1,11):
    num = int(input("Digite um número: "))
    números.append(num)

ordem = sorted(números)
print(f"O segundo maior número corresponde a {ordem[8]} e o segundo menor a {ordem[1]}")