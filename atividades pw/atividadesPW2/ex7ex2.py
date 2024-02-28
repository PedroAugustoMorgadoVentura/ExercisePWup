numero = "1234567890"
texto = str(input("Digite um número: "))
inteiro = True
for i in texto:
    if i not in numero:
        inteiro = False
        break
if inteiro == True:
    print("É inteiro")
else:
    print("Não é inteiro")