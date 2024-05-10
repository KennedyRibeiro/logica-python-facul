# Construa um algoritmo que verifique se um número fornecido pelo usuário é primo ou não.

cont = 2

n = int(input("Digite um número para ser se ele é primo: "))

while cont < n:
    if n % cont != 1:
        print("O número não é primo")
        break
    elif n % cont == 1:
        print("O número é primo!")
        break
    cont += 1




        
    
