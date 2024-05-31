#Faça um algoritmo que de posse de um vetor de N elementos inteiros, calcule e imprima a quantidade de números pares e a quantidade de números ímpares.

cont = 5
valores = [""] * cont

i = 0
par = 0
impar = 0

while i < cont:
    numeros = int(input("Digite um número: "))
    resto = numeros % 2
    
    if resto == 0:
        print("Ele é par!")
        par += 1
    else:
        print("Ele é impar!")
        impar += 1
        
    i += 1

print("A quantidade de números par é: ", par)
print("A quantidade de números impar é: ", impar)