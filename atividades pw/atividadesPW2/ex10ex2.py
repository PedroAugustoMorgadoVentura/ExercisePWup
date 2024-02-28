soma= 0
x = 0 
for i in range (0,3):
    x = int(input("Digite sua nota na avaliação de cormática: "))
    soma += x

media = soma/3

print("media: ", media)

if media  <= 60:
    print("Você está perdidinho da silva meu parceiro")
else:
    if media == 100:
        print("Olha só o novo CDF da turma brilhando")
    else:
        print("Seu pai vai dizer que não foi mais que sua obrigação passar de ano")