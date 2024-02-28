nome = input("Digite o nome do produto: ")
preco_custo = float(input("Digite o preço para produzir o produto: "))
preço_venda = float(input("Digite o preço que você vende o produto: "))
estoque = int(input("Digite a quantia do produto em estoque: "))

lucro = estoque*(preço_venda - preco_custo)

if lucro < 0:
    print(f"Você está tendo um prejuízo de R${lucro} de reais")
elif lucro > 0:
    print(f"Você está tendo um lucro de R${lucro} de reais")
else: 
    print("Nem lucro nem prejuízo")
