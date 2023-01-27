alunos = ["Francisco", "Pedro", "Henrique", "Laercio"]
notas = []

for aluno in alunos:
    for i in range(1,5):

        
        notas += input(f"Informe a nota do {i}º Semestre do {aluno}: ")

        media = sum(notas)/len(notas)
    print(media)