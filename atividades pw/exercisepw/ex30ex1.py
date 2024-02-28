conjunto1 ={1,2,3,4,5}
conjunto2 ={2,4,6,7,8}

uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)
diferenca1 = conjunto1.difference(conjunto2)
diferenca2 = conjunto2.difference(conjunto1)

print(f"Os conjuntos são: \n 1 - {conjunto1} \n 2 - {conjunto2}"
      f"\nA uniao corresponde a: {uniao} \n A interseção corresponde a: {intersecao} \n A diferença de 1 para 2 corresponde a {diferenca1} e a diferença de 2 para 1 corresponde 1 {diferenca2}")