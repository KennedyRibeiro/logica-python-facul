# Construa um algoritmo que, dado um conjunto de valores inteiros e positivos, determine qual é o menor e o maior valor do conjunto. O final da entrada de dados deve ser considerado quando o valor digitado for negativo, o qual não deve ser considerado.

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