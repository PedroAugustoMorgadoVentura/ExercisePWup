sexo = str(input("Digite seu sexo(M/H): "))
idade = int(input("Digite sua idade: "))

if sexo == "M" or "m":
    if idade >= 60:
        print("Pode aposentar-se")
    else:
        print("Ainda não pode se aposentar")
else:
    if idade >= 65:
        print("Pode aposentar-se")
    else:
        print("Ainda não pode se aposentar")