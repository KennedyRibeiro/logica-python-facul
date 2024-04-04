
cont = 1

numero = int(input("Digite um número: "))

maior = numero

while cont < 3:
    numero = int(input("Digite o próximo número: "))

    if numero > maior:
        maior = numero

    cont += 1

print("O numero maior é: ", maior)

