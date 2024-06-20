n = 4
m = 2

mat = [[""] * m for i in range(n)]

i = 0

while i < n:
    j = 0
    while j < m:
        mat[i][j] = int(input(f"Valor ({i} : {j}):"))

        j += 1

    i += 1

soma = 0
i = 0

while i < n:
    j = 0
    while j < m:
        soma += mat[i][j]

        j += 1

    i += 1

print(f"O valor da soma é :{soma}")