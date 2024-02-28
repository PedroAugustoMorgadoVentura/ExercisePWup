qtd_alunos = int(input("Digite a quantidade de alunos: "))
nota_alunos = {}

for i in range(qtd_alunos):
    nome = str(input("Nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    print("\n")
    nota_alunos[nome] = nota

nota_arredondada = {nome: round(nota) for nome, nota in nota_alunos.items()}


for nome, nota in nota_arredondada.items():
    print(f"Nome: {nome} / Nota: {nota}")