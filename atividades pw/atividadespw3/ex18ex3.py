n = int(input("Digite o valor de n para a sequência de Fibonacci: "))

fibonacci = [0, 1]

for i in range(2, n):
    next_term = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_term)

print("Sequência de Fibonacci até o", n, "termo:")
for term in fibonacci:
    print(term, end=" ")
