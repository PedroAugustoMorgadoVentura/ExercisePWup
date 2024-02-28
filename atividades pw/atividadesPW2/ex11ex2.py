temperatura = float(input("Digite a temperatura em graus Celsius: "))

if temperatura < 36:
    print("A temperatura está abaixo da faixa normal.")
elif 36 <= temperatura <= 37:
    print("A temperatura está dentro da faixa normal.")
else:
    print("A temperatura está acima da faixa normal.")
