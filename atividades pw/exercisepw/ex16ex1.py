valor_inicial = float(input("Digite o valor inicial do investimento: "))
if valor_inicial <= 0:
    print("O valor inicial do investimento deve ser positivo.")
else:
    taxa_juros = float(input("Digite a taxa de juros (em porcentagem): "))
    if taxa_juros < 0 or taxa_juros > 100:
        print("A taxa de juros deve estar entre 0% e 100%.")
    else:
        anos = int(input("Digite o número de anos: "))
        if anos <= 0:
            print("O número de anos deve ser positivo.")
        else:
            taxa_juros_decimal = taxa_juros / 100
            valor_final = valor_inicial * (1 + taxa_juros_decimal) ** anos
            print("O valor final do investimento após", anos, "anos é:", valor_final)
