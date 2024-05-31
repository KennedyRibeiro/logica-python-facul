# – Escreva um algoritmo que leia um conjunto de 20 números inteiros e mostre qual foi o maior e o menor valor fornecido.

cont = 1

numero = int(input("Digite um número: "))

maior = numero

while cont < 3:
    numero = int(input("Digite o próximo número: "))

    if numero > maior:
        maior = numero

    cont += 1

print("O numero maior é: ", maior)