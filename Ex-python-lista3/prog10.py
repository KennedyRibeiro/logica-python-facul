# Elabore um algoritmo que imprima todos os números primos existentes entre N1 e N2, em que N1 e N2 são números naturais fornecidos pelo usuário.

n1 = int(input("Qual o primeiro número ?"))
n2 = int(input("Qual o segundo número ?"))

while n1 <= n2:
    primo = 0
    metade = n1 // 2
    cont = 2
    while cont <= metade and primo == 0:
        if n1 % cont == 0:
            primo = 1
        cont += 1
    if primo == 0:
        print(n1)
    n1 =+ 1
            