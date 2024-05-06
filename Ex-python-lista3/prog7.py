# Elabore um algoritmo que calcule N! (fatorial de N), sendo que o valor inteiro de N é fornecido pelo usuário. Sabendo que

numero = int(input("Digite o número: "))

fat = 1
cont = 2

while cont <= numero:
    fat = fat * cont
    cont = cont + 1

print(fat)