numerator = int(input("Digite o numerador: "))
denominator = int(input("Digite o denominador: "))

print(f"{numerator} é divisível por {denominator}." if numerator % denominator == 0 else f"{numerator} não é divisível por {denominator}.")
