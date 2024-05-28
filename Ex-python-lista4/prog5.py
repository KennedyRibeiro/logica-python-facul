

alunos = int(input("Quantos alunos são? "))
notas1 = [""] * alunos
notas2 = [""] * alunos

i = 0

while i < alunos:
    notas1[i] = int(input("Aluno insira sua nota da prova 1: "))
    i += 1

i = 0

while i < alunos:
    notas2[i]= int(input("Aluno insira sua nota da prova 2: "))
    i += 1

i = 0

while i < alunos:
    media = (notas1[i] + notas2[i]) / 2
    print(i, media)
    i += 1



    


