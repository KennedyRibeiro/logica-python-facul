# Desenvolva um algoritmo que após armazenar valores numéricos em uma matriz N x M, calcule e mostre o somatório desses valores.

n = 4
m = 2

mat = [[""] * m for i in range (n)]

i = 0 

while i < n:
    j = 0
    while j < m:
        mat[i][j] = int(input(f"Digite o valor {i} | {j} : "))
        j += 1

    i += 1


