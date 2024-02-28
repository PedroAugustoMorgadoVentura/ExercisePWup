num = int(input("Digite um número para verificar se é primo: "))
qtd_divisores = 0

for i in range(1, num+1):
    if num%i == 0:
        qtd_divisores += 1
    else:
        continue

if qtd_divisores == 2:
    print("O número é primo")
else:
    print("O número não é primo")

