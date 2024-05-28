#  Faça um algoritmo que receba as notas da primeira prova de N alunos e armazene essas notas em um vetor. Receba as notas da segunda prova de N alunos e armazene essas notas em um outro vetor. Calcule e imprima a média entre essas duas notas de cada aluno.

alunos = int(input("Quantos alunos são? "))
notas1 = [""] * alunos
notas2 = [""] * alunos

i = 0

while i < alunos:
    notas1[i] = int(input("Aluno insira sua nota da prova 1: "))
    notas2[i]= int(input("Aluno insira sua nota da prova 2: "))
    i += 1

i = 0

while i < alunos:
    media = (notas1[i] + notas2[i]) / 2

    if media > 70:
        print(i, media, "Aprovado!")
    elif media < 50 and media > 30:
        print(i, media, "Em exame!")
    elif media < 30:
        print(i, media, "Reprovado!")
    
    i += 1