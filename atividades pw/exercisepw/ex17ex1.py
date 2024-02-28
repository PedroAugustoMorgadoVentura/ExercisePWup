preco = float(input("Digite o preço do produto: "))
imposto = float(input("Digite o imposto sobre o produto(%): "))
percent = float(input("Digite o desconto no produto(%): "))
imposto_percent = imposto/100
desconto = percent/100

preco_imposto = (preco + preco*imposto_percent)
preco_final = preco_imposto - preco_imposto*desconto

print(preco_final)