string = str(input("Escreva uma string: "))
numero = "+-/.1234567890"
real = True

for i in string:
    if i not in numero:
        real = False
        break
if real == True:
    print("A string é um número real.")
else: 
    print("A string não é um número real.")

