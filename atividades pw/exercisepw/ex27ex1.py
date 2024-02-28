nome = str(input("Qual o seu nome? "))
salario = int(input("Qual o seu salário? "))
imposto = int(input("Qual o imposto sobre seu salário(%)? "))
impostopercent = imposto/100
salario_liquido = salario - salario*impostopercent

print(f"O salário de {nome} Corresponde a R${salario_liquido} ")