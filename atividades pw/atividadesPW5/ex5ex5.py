qtd_alunos = int(input("Digite a quantidade de alunos: "))
nota_alunos = {}

for i in range(qtd_alunos):
    nome = str(input("Nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    print("\n")
    nota_alunos[nome] = nota

alunos_aprovados = {nome: nota for nome, nota in nota_alunos.items() if nota >= 7}
print("\nAlunos aprovados: \n")
for nome, nota in alunos_aprovados.items():
    print(f"Nome:{nome} / nota: {nota}")
