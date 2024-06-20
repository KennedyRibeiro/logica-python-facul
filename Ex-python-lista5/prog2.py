N = 3
M = 3

Mat = [[0]*M for i in range(N)]

i = 0
while i < N:
    j = 0
    while j < M:
        Mat[i][j] = int(input(f"Valor ({i} | {j}): "))
        j += 1
    i += 1

Menor = Mat[0][0]
Maior = Mat[0][0]
i = 0
while i < N:
    j = 0
    while j < M:
        if Mat[i][j] < Menor:
            Menor = Mat[i][j]
        else:
            if Mat[i][j] > Maior:
                Maior = Mat[i][j]
        j += 1
    i += 1

print()
i = 0
while i < N:
    j = 0
    while j < M:
        print(Mat[i][j], end = " ")
        j += 1
    print()
    i += 1

print()
print(Menor, Maior)