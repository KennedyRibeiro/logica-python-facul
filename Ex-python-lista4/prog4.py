# Faça um algoritmo que receba a temperatura média de cada mês do ano e armazene essas temperaturas em um vetor, calcule e imprima a maior e a menor temperatura do ano em que mês estas temperaturas aconteceram.

tempo = 6
temp = [""] * tempo

i = 0

while i < tempo:
    temp[i] = int(input("Qual é temperatura média desse mês ?"))
    
    i += 1

i = 0
maior = 0
menor = 999

while i < tempo:
    
    if temp[i] > maior:
        maior = temp[i]
    elif temp[i] < menor:
        menor = temp[i]
    
    i += 1

print("A maior temperatura é: ",maior,"c")
print("A menor temperatura é: ",menor,"c")