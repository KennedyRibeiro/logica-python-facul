# – Construa um algoritmo que leia um conjunto de dados contendo altura e sexo (“M” para masculino e “F” para feminino) de 50 pessoas e, depois, calcule e escreva.

m = 0
f = 0

cont = 0

menorAltF = 0
menorAltM = 0

maiorAltF = 0
maiorAltM = 0

contadorM = 0
contadorF = 0

while cont <= 50:
    sexo = input("Qual o sexo F ou M ? ")
    if sexo == "F":
        alt_f = input("Qual a sua altura ? ")
        f = alt_f
        menorAltF = alt_f
        if alt_f < menorAltF:
            menorAltF = alt_f
        else:
            maiorAltF = alt_f
        
        contadorF += 1
    elif sexo == "M":
        alt_m = input("Qual a sua altura ? ")
        m = alt_m
        menorAltM = alt_m
        if alt_f < menorAltM:
            menorAltM = alt_m
        else:  
            maiorAltM = alt_m

        contadorM += 1
    
    cont += 1

if menorAltF < menorAltM:
    print("A menor altura do grupo é: ", menorAltF)
else:
    print("A menor altura do grupo é: ", menorAltM)

if maiorAltF > maiorAltM:
    print("A maior altura do grupo é: ", maiorAltF)
else:
    print("A maior altura do grupo é: ", maiorAltM)

print("O total de homens é: ",contadorM)