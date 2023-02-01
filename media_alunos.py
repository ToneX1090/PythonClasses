alunos = ["Francisco", "Pedro", "Henrique", "Laercio"]
notas = []

for aluno in alunos:
    
    sem_1 = int(input(f"Informe a nota do primeiro semestre do {aluno}: "))
    sem_2 = int(input(f"Informe a nota do segundo semestre do {aluno}: "))

    media = (sem_1 + sem_2) / 2

    notas.append(media)

for nota in notas:

    if media <= 6:
        print(f"O {aluno} passou de ano com uma média de: {media}")
    else:
        print(f"O {aluno} reprovou de ano com uma média de: {media}")


print(notas)
    
    
    
    
    
    
    
    
    
    
    
    #for i in range(1,5):

        
     #   notas += input(f"Informe a nota do {i}º Semestre do {aluno}: ")

    #media = sum(notas)/len(notas)
    #print(media)