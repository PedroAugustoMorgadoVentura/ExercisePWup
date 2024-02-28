nomes = []

for i in range(0,10):
    nome = str(input("Digite um nome: "))
    nomes.append(nome)

caixaalta = map(lambda nome: nome.upper(), nomes)

print(list(caixaalta))