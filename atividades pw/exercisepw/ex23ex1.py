t = float(input("Digite o tempo gasto para percorrer a distância: "))
so = 0
s = float(input("Digite a distância percorrida: "))
a = float(input("Digite a aceleração: "))

#s = so + vot + at²/2
v0 = (s - so - 0.5 * a * t ** 2) / t
v = v0 + a*t

print(f"velocidade inicial: {v0}m/s \n velocidade final: {v}")
