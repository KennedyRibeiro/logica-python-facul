# Faça um algoritmo que receba a temperatura média de cada mês do ano e armazene essas temperaturas em um vetor, calcule e imprima a maior e a menor temperatura do ano em que mês estas temperaturas aconteceram.

tempo = 3
temp = [""] * tempo

i = 0

while i < tempo:
    temp[i] = float(input("Qual é temperatura média desse mês ?"))
    
    i += 1

i = 0

while i < tempo:
    maior = temp[i]
    menor = 999
    if temp[i] >= maior:
        maior = temp[i]
    
    
    i += 1


print("A maior temperatura é: ",maior)
#print("A menor temperatura é: ",menor)