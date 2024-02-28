br = input("Sua nacionalidade: ")
brasil = "brasileiro" or "Brasileiro" or "br" or "Br" or "BR"
e_brasileiro = True
for letra in br:
    if letra not in brasil:
        e_brasileiro = False

        break
if e_brasileiro == True:
    idade = int(input("Digite sua idade: "))


    if idade >= 18:
        print("Pode votar")
    else:
        print("Precisa de 18 anos para votar")
else: 
        print("É necessário ser brasileiro para votar. ")

        

    

