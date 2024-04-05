
numero = int(input("Digite um número: "))
maior = numero

while numero > 0:
    numero = int(input("Digite o próximo número: "))
    if numero > maior:
        maior = numero
    else:
        menor = numero
    
print("O maior número é: ",maior)
print("O menor numero é: ",menor)