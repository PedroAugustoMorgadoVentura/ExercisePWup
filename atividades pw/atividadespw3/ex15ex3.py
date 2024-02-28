num = int(input("Digite um número para verificar se é perfeito: "))
soma = 0

for i in range(1, num):
    if num%i == 0:
        soma += i
        print(i)
    else:
        continue

if soma == num:
    print("O número é perfeito.")
else:
    print("O número não é perfeito")




