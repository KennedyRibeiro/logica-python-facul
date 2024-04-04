# Ex para ler 3 numero e mostrar o seu maior #

cont = 1
numero = int(input("Digite um número: "))
maior = numero

while cont < 3:
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    cont += 1
    
print("O maior numero é: ",maior)


