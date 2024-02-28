primos = [2]
for num in range(3,101):
    primo = True
    for j in range(3,num):
        if num%j == 0:
            primo = False
            break
    if primo:
        primos.append(num)

print(primos)