import math
print("Calculo da queda livre")

v_inicio = float(input("Digite a velocidade no início: "))
v_fim = 0
aceleracao = 9.8

tempo = (v_inicio - v_fim)/aceleracao

print(f"O tempo para o objeto chegar ao chão é:  {tempo}")