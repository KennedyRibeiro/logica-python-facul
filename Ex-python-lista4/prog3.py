# Faça um algoritmo que receba a nota de N alunos e armazene essas notas em um vetor. Calcule e imprima:

aprovado = 0
reprovado = 0

alunos = int(input("São quantos alunos? "))
notas = [""] * alunos

b = 0

while b < alunos:
    notas[b] = float(input("Qual foi a sua nota ?"))

    if notas[b] >= 7:
        aprovado += 1
    else:
        reprovado += 1

    b += 1

b = 0
soma = 0

while b < alunos:
    soma += notas[b]

    b += 1

media = soma / alunos

print("A média da classe é: ",media)
print("Alunos aprovados são: ",aprovado)
print("Alunos reprovados são: ",reprovado)