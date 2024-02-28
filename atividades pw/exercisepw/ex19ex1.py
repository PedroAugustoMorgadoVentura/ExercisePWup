v_inicio = int(input("Digite a velocidade inicial(m/s): "))
v_fim = int(input("Digite a velocidade final(m/s): "))
tempo = int(input("Digite em segundos o tempo para atingir a velocidade final: "))

acelereção = (v_fim - v_inicio)/tempo

print(acelereção, "m/s²")