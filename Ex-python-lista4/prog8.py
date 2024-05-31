# – Faça um algoritmo que de posse de um vetor de N elementos inteiros, calcule e imprima os números primos e suas respectivas posições.

n = 4

primos = [""] * n

i = 0

while i < n:
    primos[i] = int(input("Digite um número: "))

    i += 1

i = 0

while i < n:
    cont = 1
    resto = 1
    while cont < primos[i] // 2 and resto != 0:
        resto = primos[i] % cont
        
        cont += 1

    if resto != 0:
        primos(primos[i], i)

    i += 1


