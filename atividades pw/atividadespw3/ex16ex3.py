números = []

for i in range(1,11):
    num = int(input("Digite um número: "))
    números.append(num)

ordem = sorted(números)
print(f"O maior número corresponde a {ordem[9]} e o menor a {ordem[0]}")