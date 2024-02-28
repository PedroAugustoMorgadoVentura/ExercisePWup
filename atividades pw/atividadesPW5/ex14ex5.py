nomes = input("Digite os nomes dos alunos separados por espaços: ").split()
notas = input("Digite as notas dos alunos separadas por espaços: ").split()
alunos_notas = [(nome, float(nota)) for nome, nota in zip(nomes, notas)]
alunos_notas_ordem_decrescente = sorted(alunos_notas, key=lambda x: x[1], reverse=True)
print("Lista de alunos e notas em ordem decrescente de nota:")
for aluno, nota in alunos_notas_ordem_decrescente:
    print(aluno, "-", nota)
